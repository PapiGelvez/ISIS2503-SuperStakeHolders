from django.db import models
from django.contrib.auth.hashers import MD5PasswordHasher

class Measurement(models.Model):
    trabajo = models.CharField(max_length=50, default='')
    ingresos = models.FloatField(null=True, blank=True, default=None)
    deudas = models.FloatField(null=True, blank=True, default=None)
    creditos = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return '{}'.format(self.trabajo)
    
    def hashearTrabajo(self, trabajo):
        hasher = MD5PasswordHasher() 
        trabajoHasheado = hasher.encode(self.trabajo, None)
        return trabajoHasheado
    
    def hashearIngresos(self, ingresos):
        hasher = MD5PasswordHasher() 
        ingresosHasheado = hasher.encode(self.ingresos, None)
        return ingresosHasheado
    
    def hashearDeudas(self, deudas):
        hasher = MD5PasswordHasher() 
        deudasHasheado = hasher.encode(self.deudas, None)
        return deudasHasheado
    
    def hashearCreditos(self, creditos):
        hasher = MD5PasswordHasher() 
        creditosHasheado = hasher.encode(self.creditos, None)
        return creditosHasheado
    
    def save(self, *args, **kwargs):
        self.trabajo = self.hashearTrabajo(self.trabajo)
        self.ingresos = self.hashearIngresos(self.ingresos)
        self.deudas = self.hashearDeudas(self.deudas)
        self.creditos = self.hashearCreditos(self.creditos)
        super(Measurement, self).save(*args, **kwargs)
        
    