from django.db import models

familia=( ('Aceráceas','Aceráceas'), ('Anacardiáceas','Anacardiáceas'), ('Aquifoliáceas','Aquifoliáceas'), ('Betuláceas','Betuláceas'), ('Buxáceas','Buxáceas'), ('Caprifoliáceas','Caprifoliáceas'),('Celastráceas','Celastráceas'),('Cornáceas','Cornáceas'),('Cupresáceas','Cupresáceas'),('Eleagnáceas','Eleagnáceas'),('Ericácas','Ericácas'),('Fagáceas','Fagáceas'),('Juglandáceas','Juglandáceas'),('Lauráceas','Lauráceas'),('Leguminosas','Leguminosas'),('Meliáceas','Meliáceas'),('Mirtáceas','Mirtáceas'),('Moráceas','Moráceas'),('Oleáceas','Oleáceas'),('Palmáceas','Palmáceas'),('Pináceas','Pináceas'),('Platanáceas','Platanáceas'),('Punicáceas','Punicáceas'),('Ramnáceas','Ramnáceas'),('Rosáceas','Rosáceas'),('Salicáceas','Salicáceas'),('Simaroubáceas','Simaroubáceas'),('Solanáceas','Solanáceas'),('Tamariacáceas','Tamariacáceas'),('Taxáceas','Taxáceas'),('Tiliáceas','Tiliáceas'),('Ulmáceas','Ulmáceas'),)

motivo_singularidad=( ('Antigüedad','Antigüedad'), ('Elevado Diámetro','Elevado Diámetro'), ('Plantado por un personaje histórico','Plantado por un personaje histórico'),('Vistosidad','Vistosidad'),('Madera codiciada','Madera codiciada'),('Frutos peculiares','Frutos peculiares'), ('Utilidad medicinal','Utilidad medicinal'))

class Familia(models.Model):
    idFamilia = models.AutoField('ID',primary_key=True, serialize=False)
    nombreFamilia = models.CharField('Nombre', unique=True, blank=False, choices=familia, max_length=30)

class Genero(models.Model):
    idGenero = models.AutoField('ID',primary_key=True, serialize=False)
    nombreGenero = models.CharField('Nombre', unique=True, blank=False, max_length=30)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

class Especie(models.Model):
    idEspecie = models.AutoField('ID',primary_key=True, serialize=False)
    nombreCientificoEspecie = models.CharField('Nombre Cientifico', unique=True, blank=False,  max_length=30)
    nombreComunEspecie = models.CharField('Nombre Común', unique=True, blank=False,  max_length=30)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autoctona = models.BooleanField('Autóctona', default=False)
    descripcion = models.TextField('Descripcion', blank=False)
    ecologia = models.TextField('Ecologia', blank=False)

class Individuos(models.Model):
    idIndividuo = models.AutoField('ID',primary_key=True, serialize=False)
    nombreComun = models.CharField('Nombre Común', unique=True, blank=False,  max_length=30)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    motivoSingular = models.CharField('Motivo de Singularidad',choices=motivo_singularidad, blank=False, max_length=50)
    explicacionMotivoSingular = models.TextField('Explicacion de Singularidad',blank=False)
    x = models.DecimalField ('X',blank=False, default=1,max_digits=19, decimal_places=15)
    y = models.DecimalField ('Y',blank=False,default=1,max_digits=19, decimal_places=15)
    fotoArbol = models.ImageField(upload_to='static/imagenes',blank=False)
    fotoHojas = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoTronco = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoFrutos = models.ImageField(upload_to='static/imagenes',blank=True)
    altura = models.DecimalField('Altura',blank=False, default=0,max_digits=19, decimal_places=15)
    perimetro = models.DecimalField('Perimetro',blank=False, default=0,max_digits=19, decimal_places=15)


permisos=(('Administrador','Administrador'), ('Usuario','Usuario'),)

class Usuario(models.Model):
    idUsuario = models.AutoField('ID',primary_key=True, serialize=False)
    nombreUsuario = models.CharField('Nombre',blank=False,max_length=30,unique=True)
    primerApellido = models.CharField('Primer Apellido',blank=False,max_length=30)
    segundoApellido = models.CharField('Segundo Apellido',blank=False,max_length=30)
    email = models.EmailField('E-mail',blank=False,unique=True)
    contrasenia = models.CharField('Contraseña',blank=False,max_length=30)
    tipo = models.CharField('Tipo',blank=False,choices=permisos,max_length=30, default='Usuario')
    activo = models.BooleanField('Activo', default=False)
