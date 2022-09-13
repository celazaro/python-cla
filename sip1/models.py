from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    habitacion = models.IntegerField(verbose_name='Habitación',null=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=30)
    apellido = models.CharField(verbose_name='Apellido', max_length=30)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    diagnostico = models.CharField(verbose_name='Diagnóstico', max_length=100)
    comida = models.TextField(verbose_name='Comida', null=True)

    def __str__(self):
        fila="Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    