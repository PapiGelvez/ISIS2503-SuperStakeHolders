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

    def save(self):
        measurement = super(MeasurementForm, self).save(commit=False)
        measurement.trabajo = measurement.hashearTrabajo(self.cleaned_data['trabajo'])
        #measurement.ingresos = measurement.hashearIngresos(self.cleaned_data['ingresos'])
        #measurement.deudas = measurement.hashearDeudas(self.cleaned_data['deudas'])
        #measurement.creditos = measurement.hashearCreditos(self.cleaned_data['creditos'])

        measurement.save()
        return measurement