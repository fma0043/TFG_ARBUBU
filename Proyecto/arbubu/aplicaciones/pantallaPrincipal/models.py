from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField('Nombre', max_length=80)
    descripcion = models.TextField('Descripcion', blank=True)
    ecologia = models.TextField('Ecologia',blank=True)
    distribucion = models.TextField('Distribucion',blank=True)

    def __str__(self):
        return self.nombreFamilia

class Especie(models.Model):
    nombreEspecie = models.CharField('nombre_Especie', blank=False, max_length=80)
    caracteristicas = models.TextField('Caracteristicas',blank=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    def __str__(self):
            return self.nombreEspecie

class Individuos(models.Model):
    nombreIndividuos = models.CharField('nombre_Individuos', blank=False, max_length=80)
    caracteristicas = models.TextField('Caracteristicas',blank=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    def __str__(self):
            return self.nombreIndividuos
