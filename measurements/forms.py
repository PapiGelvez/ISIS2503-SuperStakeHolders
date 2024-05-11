from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'trabajo',
            'ingresos',
            'deudas',
            'creditos',
        ]

        labels = {
            'trabajo' : 'Trabajo',
            'ingresos' : 'Ingresos',
            'deudas' : 'Deudas',
            'creditos' : 'Creditos',
        }

    def obtener_y_descifrar_datos():
        # Obtener los objetos Measurement de la base de datos
        measurements= Measurement.objects.all()

        # Descifrar los valores de ingresos de cada objeto Measurement
        ingresos_descifrados = []
        for measurement in measurements:
            ingresos_descifrados.append(Measurement().descifrar_valor(measurement.ingresos, '333333'))

        return ingresos_descifrados

    if __name__ == '__main__':
        datos_descifrados = obtener_y_descifrar_datos()
        print(datos_descifrados)

    def save(self, commit=True):
        measurement = super(MeasurementForm, self).save(commit=False)
        #measurement.trabajo = measurement.cifrar_valor(self.cleaned_data['trabajo'])
        measurement.ingresos = measurement.cifrar_valor(self.cleaned_data['ingresos'])
        measurement.deudas = measurement.cifrar_valor(self.cleaned_data['deudas'])
        measurement.creditos = measurement.cifrar_valor(self.cleaned_data['creditos'])
        if commit:
            measurement.save()
        return measurement


