from django.db import models

#import crypt

familia=( ('Aceráceas','Aceráceas'), ('Anacardiáceas','Anacardiáceas'), ('Aquifoliáceas','Aquifoliáceas'), ('Betuláceas','Betuláceas'), ('Buxáceas','Buxáceas'), ('Caprifoliáceas','Caprifoliáceas'),('Celastráceas','Celastráceas'),('Cornáceas','Cornáceas'),('Cupresáceas','Cupresáceas'),('Eleagnáceas','Eleagnáceas'),('Ericácas','Ericácas'),('Fagáceas','Fagáceas'),('Juglandáceas','Juglandáceas'),('Lauráceas','Lauráceas'),('Leguminosas','Leguminosas'),('Meliáceas','Meliáceas'),('Mirtáceas','Mirtáceas'),('Moráceas','Moráceas'),('Oleáceas','Oleáceas'),('Palmáceas','Palmáceas'),('Pináceas','Pináceas'),('Platanáceas','Platanáceas'),('Punicáceas','Punicáceas'),('Ramnáceas','Ramnáceas'),('Rosáceas','Rosáceas'),('Salicáceas','Salicáceas'),('Simaroubáceas','Simaroubáceas'),('Solanáceas','Solanáceas'),('Tamariacáceas','Tamariacáceas'),('Taxáceas','Taxáceas'),('Tiliáceas','Tiliáceas'),('Ulmáceas','Ulmáceas'),)

motivo_singularidad=( ('Antigüedad','Antigüedad'), ('Elevado Diámetro','Elevado Diámetro'), ('Plantado por un personaje histórico','Plantado por un personaje histórico'),('Vistosidad','Vistosidad'),('Madera codiciada','Madera codiciada'),('Frutos peculiares','Frutos peculiares'), ('Utilidad medicinal','Utilidad medicinal'))

class Familia(models.Model):
    nombreFamilia = models.CharField('Nombre', unique=True, blank=False, choices=familia, max_length=30)

    def __str__(self):
        return self.nombreFamilia

class Especie(models.Model):

    nombreCientificoEspecie = models.CharField('Nombre Cientifico', unique=True, blank=False,  max_length=30)
    nombreComunEspecie = models.CharField('Nombre Común', unique=True, blank=False,  max_length=30)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    autoctona = models.BooleanField('Autóctona', default=False)
    descripcion = models.TextField('Descripcion', blank=False)
    ecologia = models.TextField('Ecologia', blank=False)

    def __str__(self):
        return self.nombreCientificoEspecie


class Individuos(models.Model):
    nombreComun = models.ForeignKey(Especie, on_delete=models.CASCADE)
    motivoSingular = models.CharField('Motivo de Singularidad',choices=motivo_singularidad, blank=False, max_length=50)
    explicacionMotivoSingular = models.TextField('Explicacion de Singularidad',blank=False)
    x = models.IntegerField('X',blank=False, default=1)
    y = models.IntegerField('Y',blank=False,default=1)
    fotoArbol = models.ImageField(upload_to='static/imagenes',blank=False)
    fotoHojas = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoTronco = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoFrutos = models.ImageField(upload_to='static/imagenes',blank=True)
    altura = models.IntegerField('Altura',blank=False, default=0)
    perimetro = models.IntegerField('Perimetro',blank=False, default=0)

    def __str__(self):
        return self.nombreComun

permisos=(('Administrador','Administrador'), ('Usuario','Usuario'),)

class Usuario(models.Model):
    nombreUsuario = models.CharField('Nombre',blank=False,max_length=30,unique=True)
    primerApellido = models.CharField('Primer Apellido',blank=False,max_length=30)
    segundoApellido = models.CharField('Segundo Apellido',blank=False,max_length=30)
    email = models.EmailField('E-mail',blank=False,unique=True)
    contrasenia = models.CharField('Contraseña',blank=False,max_length=30)
    tipo = models.CharField('Tipo',blank=False,choices=permisos,max_length=30, default='Usuario')
    activo = models.BooleanField('Activo', default=False)

    def __str__(self):
            return self.nombreUsuario

class _Familias(object):

    def __init__(self,nombreFamilia):
        self.nombreFamilia = nombreFamilia

    def getNombreFamilia(self):
        return self.nombreFamilia

    def setNombreFamilia(self, nombreFamilia):
        self.nombreFamilia = nombreFamilia

    def devolverFamilias(self):
        familias = list()
        for i in range (self.nombreFamilia):
            familias.append(i)
        return familias

class _Especies(object):

    def __init__(self,nombreCientificoEspecie,nombreComunEspecie,familia,autoctona,descripcion,ecologia):
        self.nombreCientificoEspecie = nombreCientificoEspecie
        self.nombreComunEspecie = nombreComunEspecie
        self.familia = familia
        self.autoctona = autoctona
        self.descripcion = descripcion
        self.ecologia = ecologia

    def __str__(self):
        return self.nombreCientificoEspecie

    def getNombreCientificoEspecie(self):
        return self.nombreCientificoEspecie

    def setNombreCientificoEspecie(self, _nombreCientificoEspecie):
        self.nombreCientificoEspecie = _nombreCientificoEspecie

    def getNombreComunEspecie(self):
        return self.nombreComunEspecie

    def setNombreComunEspecie(self, _nombreComunEspecie):
        self.nombreComunEspecie = _nombreComunEspecie

    def getFamilia(self):
        return self.familia

    def setFamilia(self, _familia):
        self.familia = _familia

    def getAutoctona(self):
        return self.autoctona

    def setAutoctona(self, _autoctona):
        self.autoctona = _autoctona

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, _descripcion):
        self.descripcion = _descripcion

    def getEcologia(self):
        return self.ecologia

    def setEcologia(self, _ecologia):
        self.ecologia = _ecologia

    def devolverEspeciesPorNombreCientificoEspecie(self):
        especies = list()
        for i in range (self.nombreCientificoEspecie):
            especies.append(i)
        return especies

    def devolverEspeciesPorNombreComunEspecie(self):
        especies = list()
        for i in range (self.nombreComunEspecie):
            especies.append(i)
        return especies

    def devolverEspeciesPorAutoctona(self):
        especies = list()
        for i in range (self.autoctona):
            if self.autoctona == True:
                especies.append(i)
        return especies

class _Individuos(object):

    def __init__(self,nombreComun,motivoSingular,explicacionMotivoSingular,x,y,altura,perimetro):
        self.nombreComun = nombreComun
        self.motivoSingular = motivoSingular
        self.explicacionMotivoSingular = explicacionMotivoSingular
        self.x = x
        self.y = y
        self.altura = altura
        self.perimetro = perimetro

    def __str__(self):
        return self.nombreComun

    def getNombreComun(self):
        return self.nombreComun

    def setNombreComun(self, _nombreComun):
        self.nombreComun = _nombreComun

    def getMotivoSingular(self):
        return self.motivoSingular

    def setMotivoSingular(self, _motivoSingular):
        self.motivoSingular = _motivoSingular

    def getExplicacionMotivoSingular(self):
        return self.explicacionMotivoSingular

    def setMotivoSingular(self, _explicacionMotivoSingular):
        self.explicacionMotivoSingular = _explicacionMotivoSingular

    def getX(self):
        return self.x

    def setX(self, _x):
        self.x = _x

    def getY(self):
        return self.y

    def setY(self, _y):
        self.y = _y

    def getAltura(self):
        return self.altura

    def setAltura(self, _altura):
        self.altura = _altura

    def getPerimetro(self):
        return self.perimetro

    def setPerimetro(self, _perimetro):
        self.perimetro = _perimetro

    def devolverIndividuosPorMotivoSingular(self):
        individuo = list()
        for i in range (self.motivoSingular):
            individuo.append(i)
        return individuo

    def devolverIndividuoPorAltura(self):
        individuo = list()
        for i in range (self.altura):
            individuo.append(i)
        return individuo

    def devolverIndividuoPorPerimetro(self):
        individuo = list()
        for i in range (self.perimetro):
            individuo.append(i)
        return individuo

class _Usuario(object):

    def __init__(self,nombreUsuario,primerApellido,segundoApellido,email,contrasenia,tipo,activo):
        self.nombreUsuario = nombreUsuario
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.email = email
        self.y = y
        self.contrasenia = contrasenia
        self.tipo = tipo
        self.activo = activo

    def __str__(self):
            return self.nombreUsuario

    def permisosAdmin(self):
        usuario = list()
        for i in range (self.tipo):
            if self.tipo == Administrador:
                usuario.append(i)
        return usuario
