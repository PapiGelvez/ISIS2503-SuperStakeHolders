from django.db import models
from django.contrib.auth.hashers import MD5PasswordHasher
import hashlib

class Measurement(models.Model):
    trabajo = models.CharField(max_length=50, default='')
    ingresos = models.FloatField(null=True, blank=True, default=None)
    deudas = models.FloatField(null=True, blank=True, default=None)
    creditos = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return '{}'.format(self.trabajo)
    
    def hashearTrabajo(self, trabajo):
        hasher = MD5PasswordHasher() 
        trabajoHasheado = hashlib.md5((self.trabajo).encode()).hexdigest()
        new_string = trabajoHasheado[6:]
        return trabajoHasheado
    
    def hashearIngresos(self):
        hasher = MD5PasswordHasher() 
        ingresosHasheado = hasher.encode(self.ingresos, " ")
        new_string = ingresosHasheado[6:]
        return new_string
    
    def hashearDeudas(self):
        hasher = MD5PasswordHasher() 
        deudasHasheado = hasher.encode(self.deudas, " ")
        new_string = deudasHasheado[6:]
        return new_string
    
    def hashearCreditos(self):
        hasher = MD5PasswordHasher() 
        creditosHasheado = hasher.encode(self.creditos, " ")
        new_string = creditosHasheado[6:]
        return new_string
    
    def save(self, *args, **kwargs):
        self.trabajo = self.hashearTrabajo(self.trabajo)
        #self.ingresos = self.hashearIngresos(self.ingresos)
        #self.deudas = self.hashearDeudas(self.deudas)
        #self.creditos = self.hashearCreditos(self.creditos)
        super(Measurement, self).save(*args, **kwargs)
        
    