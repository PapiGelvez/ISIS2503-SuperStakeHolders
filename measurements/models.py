from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash

class Measurement(models.Model):
    trabajo = models.CharField(max_length=200, default='')
    ingresos = models.CharField(max_length=200, default='')
    deudas = models.CharField(max_length=200, default='')
    creditos = models.CharField(max_length=200, default='')
    
    def cifrar_valor(self, valor):
        return generate_password_hash(str(valor))

    def descifrar_valor(self, valor_hash, valor):
        return check_password_hash(valor_hash, str(valor))

    def save(self, *args, **kwargs):
        #self.trabajo = self.cifrar_valor(self.trabajo)
        self.ingresos = self.cifrar_valor(self.ingresos)
        self.deudas = self.cifrar_valor(self.deudas)
        self.creditos = self.cifrar_valor(self.creditos)
        super(Measurement, self).save(*args, **kwargs)
