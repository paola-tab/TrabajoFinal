from django.db import models
from django.utils import timezone


class Persona(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    direccion= models.CharField(max_length=100)
    fecha_nacimiento= models.DateTimeField()
    fecha_de_alta= models.DateTimeField(
            default= timezone.now)
    published_date= models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.apellido + ', ' + self.nombre 


