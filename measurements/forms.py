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
        
        #measurement.trabajo = measurement.cifrar_valor(self.cleaned_data['trabajo'])
       # arreglo_ingresos.append(measurement.ingresos)
        #measurement.ingresos = measurement.cifrar_valor(self.cleaned_data['ingresos'])
        #arreglo_deudas.append(measurement.deudas)
       # measurement.deudas = measurement.cifrar_valor(self.cleaned_data['deudas'])
        #arreglo_creditos.append(measurement.creditos)
        #measurement.creditos = measurement.cifrar_valor(self.cleaned_data['creditos'])
       # if commit:
        #measurement.save()
        return measurement
    