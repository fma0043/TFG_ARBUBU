from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField('Nombre',unique=True, max_length=30,blank=False)

    def __str__(self):
        return self.nombre

class Especie(models.Model):
    nombreCientifico = models.CharField('Nombre Cientifico', unique=True,blank=False, max_length=30)
    nombreComun = models.CharField('Nombre Común', unique=True,blank=False, max_length=30)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=False)
    autoctona = models.BooleanField('Autóctona', default=False)
    distribucion = models.TextField('Distribucion', blank=False)
    descripcion = models.TextField('Descripcion', blank=False)
    ecologia = models.TextField('Ecologia', blank=False)
    masInfo = models.TextField('Más Información', blank=False)

    def __str__(self):
            return self.nombreCientifico

class Individuos(models.Model):
    nombre = models.CharField('Nombre',unique=True,blank=False,max_length=30)
    motivoSingular = models.TextField('Motivo de Singularidad',blank=False)
    x = models.IntegerField('X',blank=False, default=1)
    y = models.IntegerField('Y',blank=False,default=1)
    fotoArbol = models.ImageField(upload_to='templates/pantallaPrincipal',blank=False)
    fotoHojas = models.ImageField(upload_to='templates/pantallaPrincipal',blank=True)
    fotoTronco = models.ImageField(upload_to='templates/pantallaPrincipal',blank=True)
    fotoFrutos = models.ImageField(upload_to='templates/pantallaPrincipal',blank=True)
    altura = models.IntegerField('Altura',blank=False, default=1)
    perimetro = models.IntegerField('Perimetro',blank=False, default=1)

    def __str__(self):
            return self.nombre

#especie = models.ForeignKey(Especie, on_delete=models.CASCADE,blank=False)

#<td><a href="{% url 'pantallaPrincipal_app:lista-individuo' l.id %}">Ver Individuo</a></td>
