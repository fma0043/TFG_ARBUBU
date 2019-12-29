from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

familia=( ('Aceráceas','Aceráceas'), ('Adoxáceas','Adoxáceas'), ('Anacardiáceas','Anacardiáceas'), ('Aquifoliáceas','Aquifoliáceas'), ('Araliáceas','Araliáceas'), ('Betuláceas','Betuláceas'), ('Buxáceas','Buxáceas'), ('Bignoniáceas','Bignoniáceas'), ('Caprifoliáceas','Caprifoliáceas'),('Celastráceas','Celastráceas'),('Cornáceas','Cornáceas'),('Cupresáceas','Cupresáceas'),('Eleagnáceas','Eleagnáceas'),('Ericácas','Ericácas'),('Fagáceas','Fagáceas'),('Fabaceaes','Fabaceaes'),('Juglandáceas','Juglandáceas'),('Lauráceas','Lauráceas'),('Leguminosas','Leguminosas'),('Magnoliáceas','Magnoliáceas'), ('Malvaceae','Malvaceae'),('Meliáceas','Meliáceas'),('Mirtáceas','Mirtáceas'),('Moráceas','Moráceas'),('Oleáceas','Oleáceas'),('Palmáceas','Palmáceas'),('Pináceas','Pináceas'),('Pinus','Pinus'),('Platanáceas','Platanáceas'),('Punicáceas','Punicáceas'),('Ramnáceas','Ramnáceas'),('Rosáceas','Rosáceas'),('Salicáceas','Salicáceas'),('Simaroubáceas','Simaroubáceas'),('Solanáceas','Solanáceas'),('Tamariacáceas','Tamariacáceas'),('Taxáceas','Taxáceas'),('Tiliáceas','Tiliáceas'),('Ulmáceas','Ulmáceas'),)

motivo_singularidad=( ('Antigüedad','Antigüedad'), ('Elevado Diámetro','Elevado Diámetro'), ('Plantado por un personaje histórico','Plantado por un personaje histórico'),('Vistosidad','Vistosidad'),('Madera codiciada','Madera codiciada'),('Frutos peculiares','Frutos peculiares'), ('Utilidad medicinal','Utilidad medicinal'))

class Familia(models.Model):
    idFamilia = models.AutoField('ID',primary_key=True, serialize=False)
    nombreFamilia = models.CharField('Nombre', unique=True, blank=False, choices=familia, max_length=30)

    class Meta:
        ordering = ['nombreFamilia']

class Genero(models.Model):
    idGenero = models.AutoField('ID',primary_key=True, serialize=False)
    nombreGenero = models.CharField('Nombre', unique=True, blank=False, max_length=30)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nombreGenero']

class Especie(models.Model):
    idEspecie = models.AutoField('ID',primary_key=True, serialize=False)
    nombreCientificoEspecie = models.CharField('Nombre Cientifico', blank=False,  max_length=50)
    nombreComunEspecie = models.CharField('Nombre Común',  blank=False,  max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autoctona = models.BooleanField('Autóctona', default=False)
    descripcion = models.TextField('Descripcion', blank=False)
    ecologia = models.TextField('Ecologia', blank=False)

    class Meta:
        ordering = ['nombreCientificoEspecie']

ubicacion=( ('Campus Río Vena','Campus Río Vena'), ('Hospital del Rey','Hospital del Rey'), ('Hospital Militar','Hospital Militar'),('Campus de Educación','Campus de Educación'),('Campus de Ciencias','Campus de Ciencias'))

class Individuos(models.Model):
    idIndividuo = models.AutoField('ID',primary_key=True, serialize=False)
    nombreComun = models.CharField('Nombre Común', blank=True, max_length=30)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    motivoSingular = models.CharField('Motivo de Singularidad',choices=motivo_singularidad, blank=False, max_length=50)
    explicacionMotivoSingular = models.TextField('Explicacion de Singularidad',blank=False)
    latitud = models.DecimalField ('Latitud',blank=False, default=1,max_digits=11, decimal_places=7)
    longitud = models.DecimalField ('Longitud',blank=False,default=1,max_digits=11, decimal_places=9)
    fotoArbol = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoHojas = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoTronco = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoFrutos = models.ImageField(upload_to='static/imagenes',blank=True)
    ubicacion = models.CharField('Ubicación', choices=ubicacion, blank=False, max_length=50 )
    altura = models.DecimalField('Altura',blank=False, default=0,max_digits=19, decimal_places=15)
    perimetro = models.DecimalField('Perimetro',blank=False, default=0,max_digits=19, decimal_places=15)

    class Meta:
        ordering = ['nombreComun']

    def __str__(self):
        return self.nombreComun

class Usuario(models.Model):
    idUsuario = models.AutoField('ID',primary_key=True, serialize=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.usuario.save()
