from django.db import models
#import crypt

# Create your models here.
familias=( ('AC','Aceráceas'), ('AN','Anacardiáceas'), ('AQ','Aquifoliáceas'), ('BE','Betuláceas'), ('BU','Buxáceas'), ('CA','Caprifoliáceas'),('CE','Celastráceas'),('CO','Cornáceas'),('CU','Cupresáceas'),('EL','Eleagnáceas'),('ER','Ericácas'),('FA','Fagáceas'),('JU','Juglandáceas'),('LA','Lauráceas'),('LE','Leguminosas'),('ME','Meliáceas'),('MI','Mirtáceas'),('MO','Moráceas'),('OL','Oleáceas'),('PA','Palmáceas'),('PI','Pináceas'),('PL','Platanáceas'),('PU','Punicáceas'),('RA','Ramnáceas'),('RO','Rosáceas'),('SA','Salicáceas'),('SI','Simaroubáceas'),('SO','Solanáceas'),('TA','Tamariacáceas'),('TA','Taxáceas'),('TI','Tiliáceas'),('UL','Ulmáceas'),)

motivo_singularidad=( ('AN','Antigüedad'), ('DI','Elevado Diámetro'), ('HI','Lo plantó un personaje histórico'),)

distribucion_predominante=( ('AS','Asia'), ('AN','Antártida'), ('EU','Europa'), ('AF','África'), ('OC','Oceanía'), ('AM','América'),)

class Familia(models.Model):
    nombre = models.CharField('Nombre',unique=True,choices=familias, max_length=30,blank=False)

    def __str__(self):
        return self.nombre

class Especie(models.Model):
    nombreCientifico = models.CharField('Nombre Cientifico', unique=True,blank=False, max_length=30)
    nombreComun = models.CharField('Nombre Común', unique=True,blank=False, max_length=30)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=False)
    autoctona = models.BooleanField('Autóctona', default=False)
    distribucion = models.CharField('Distribucion', max_length=30,choices=distribucion_predominante,blank=False)
    descripcion = models.TextField('Descripcion', blank=False)
    ecologia = models.TextField('Ecologia', blank=False)
    masInfo = models.TextField('Más Información', blank=False)

    def __str__(self):
            return self.nombreCientifico

class Individuos(models.Model):
    nombre = models.CharField('Nombre',unique=True,blank=False,max_length=30)
    motivoSingular = models.TextField('Motivo de Singularidad',choices=motivo_singularidad, blank=False)
    x = models.IntegerField('X',blank=False, default=1)
    y = models.IntegerField('Y',blank=False,default=1)
    tipoEspecie = models.ForeignKey(Especie, on_delete=models.CASCADE, blank=False)
    fotoArbol = models.ImageField(upload_to='static/imagenes',blank=False)
    fotoHojas = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoTronco = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoFrutos = models.ImageField(upload_to='static/imagenes',blank=True)
    altura = models.IntegerField('Altura',blank=False, default=1)
    perimetro = models.IntegerField('Perimetro',blank=False, default=1)

    def __str__(self):
            return self.nombre

class Usuario(models.Model):
    nombre = models.CharField('Nombre',blank=False,max_length=30)
    primerApellido = models.CharField('Primer Apellido',blank=False,max_length=30,default="")
    segundoApellido = models.CharField('Segundo Apellido',blank=False,max_length=30,default="")
    email = models.EmailField('E-mail',default="")
    contrasenia = models.CharField('Contraseña',blank=False,max_length=30,default="")


    def __str__(self):
            return self.nombre

    def encriptarContrasenia(self):
        contraseniaEncriptada=crypt.crypt(self.contrasenia, 'salt')
        return contraseniaEncriptada
