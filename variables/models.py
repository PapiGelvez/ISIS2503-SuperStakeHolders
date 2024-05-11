from django.db import models
import hashlib

class Variable(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='Colombia')
    city = models.CharField(max_length=50, default='Bogota')
    phone = models.IntegerField(default=123456789)
    mail = models.CharField(max_length=50, default='@bancodelosalpes.com.co')

    def __str__(self):
        return '{}'.format(self.name)

    def hashear(self, valor):
        hash = hashlib.md5((valor).encode()).hexdigest()
        return hash
    
    def save(self, *args, **kwargs):
        self.name = self.cifrar_valor(self.name)
        self.lastname = self.cifrar_valor(self.lastname)
        self.country = self.cifrar_valor(self.country)
        self.city = self.cifrar_valor(self.city)
        super(Variable, self).save(*args, **kwargs)