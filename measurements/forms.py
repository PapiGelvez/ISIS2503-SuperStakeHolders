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

    def save(self, commit=True):
        measurement = super(MeasurementForm, self).save(commit=False)
        measurement.ingresos_hash = measurement.cifrar_valor(self.cleaned_data['ingresos'])
        measurement.deudas_hash = measurement.cifrar_valor(self.cleaned_data['deudas'])
        measurement.creditos_hash = measurement.cifrar_valor(self.cleaned_data['creditos'])
        if commit:
            measurement.save()
        return measurement
