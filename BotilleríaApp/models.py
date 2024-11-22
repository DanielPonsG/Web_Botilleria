from django.db import models

# Create your models here.
class Botellas(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True)
    cantidad = models.IntegerField()
    imagen = models.ImageField(null=False)


