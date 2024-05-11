from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash

class Measurement(models.Model):
    trabajo = models.CharField(max_length=50, default='')
    ingresos = models.FloatField(null=True, blank=True, default=None)
    deudas = models.FloatField(null=True, blank=True, default=None)
    creditos = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.trabajo)


    def cifrar_valor(self, valor):
        return generate_password_hash(str(valor))

    def descifrar_valor(self, valor_hash, valor):
        return check_password_hash(valor_hash, str(valor))

    def save(self, *args, **kwargs):
        self.ingresos = self.cifrar_valor(self.ingresos)
        self.deudas = self.cifrar_valor(self.deudas)
        self.creditos = self.cifrar_valor(self.creditos)
        super(Measurement, self).save(*args, **kwargs)
