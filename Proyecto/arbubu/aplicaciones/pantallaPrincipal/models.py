from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField('Nombre', max_length=80)
    descripcion = models.CharField('Descripcion', blank=True, max_length=200)
    ecologia = models.CharField('Ecologia',blank=True, max_length=200)
    distribucion = models.CharField('Distribucion',blank=True, max_length=200)

    def __str__(self):
        return self.nombreFamilia

class Especie(models.Model):
    nombreEspecie = models.CharField('nombre_Especie', blank=False, max_length=80)
    caracteristicas = models.TextField('Caracteristicas',blank=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    def __str__(self):
            return self.nombreEspecie
