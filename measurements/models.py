from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash

class Measurement(models.Model):
    trabajo = models.CharField(max_length=50, default='')
    ingresos_hash = models.CharField(max_length=128, null=True, blank=True, default=None)
    deudas_hash = models.CharField(max_length=128, null=True, blank=True, default=None)
    creditos_hash = models.CharField(max_length=128, null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.trabajo)

    def cifrar_valor(self, valor):
        return generate_password_hash(str(valor))

    def descifrar_valor(self, valor_hash, valor):
        return check_password_hash(valor_hash, str(valor))

    def save(self, *args, **kwargs):
        self.ingresos_hash = self.cifrar_valor(self.ingresos)
        self.deudas_hash = self.cifrar_valor(self.deudas)
        self.creditos_hash = self.cifrar_valor(self.creditos)
        super(Measurement, self).save(*args, **kwargs)
