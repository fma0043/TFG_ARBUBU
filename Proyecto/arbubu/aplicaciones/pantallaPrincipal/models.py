from django.db import models

#import crypt


familias=( ('Aceráceas','Aceráceas'), ('Anacardiáceas','Anacardiáceas'), ('Aquifoliáceas','Aquifoliáceas'), ('Betuláceas','Betuláceas'), ('Buxáceas','Buxáceas'), ('Caprifoliáceas','Caprifoliáceas'),('Celastráceas','Celastráceas'),('Cornáceas','Cornáceas'),('Cupresáceas','Cupresáceas'),('Eleagnáceas','Eleagnáceas'),('Ericácas','Ericácas'),('Fagáceas','Fagáceas'),('Juglandáceas','Juglandáceas'),('Lauráceas','Lauráceas'),('Leguminosas','Leguminosas'),('Meliáceas','Meliáceas'),('Mirtáceas','Mirtáceas'),('Moráceas','Moráceas'),('Oleáceas','Oleáceas'),('Palmáceas','Palmáceas'),('Pináceas','Pináceas'),('Platanáceas','Platanáceas'),('Punicáceas','Punicáceas'),('Ramnáceas','Ramnáceas'),('Rosáceas','Rosáceas'),('Salicáceas','Salicáceas'),('Simaroubáceas','Simaroubáceas'),('Solanáceas','Solanáceas'),('Tamariacáceas','Tamariacáceas'),('Taxáceas','Taxáceas'),('Tiliáceas','Tiliáceas'),('Ulmáceas','Ulmáceas'),)

motivo_singularidad=( ('Antigüedad','Antigüedad'), ('Elevado Diámetro','Elevado Diámetro'), ('Plantado por un personaje histórico','Plantado por un personaje histórico'),('Vistosidad','Vistosidad'),('Madera codiciada','Madera codiciada'),('Frutos peculiares','Frutos peculiares'), ('Utilidad medicinal','Utilidad medicinal'))

class Familia(models.Model):
    nombreFamilia = models.CharField('Nombre',unique=True,choices=familias, max_length=30,blank=False)

    def __str__(self):
        return self.nombreFamilia

    def __init__(self, nombreFamilia):
        self.__nombreFamilia = nombreFamilia

    def getNombreFamilia(self):
        return self.__nombreFamilia

    def setNombreFamilia(self, nombreFamilia):
        self.__nombreFamilia = nombreFamilia

    def devolverFamilias(self):
        familias = list()
        for i in range (self.nombreFamilia):
            familias.append(i)
        return familias

class Especie(models.Model):
    nombreCientificoEspecie = models.CharField('Nombre Cientifico', unique=True,blank=False, max_length=30)
    nombreComunEspecie = models.CharField('Nombre Común', unique=True,blank=False, max_length=30)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=False)
    autoctona = models.BooleanField('Autóctona', default=False)
    descripcion = models.TextField('Descripcion', blank=False)
    ecologia = models.TextField('Ecologia', blank=False)

    def __str__(self):
            return self.nombreComunEspecie

    def __init__(self, nombreCientificoEspecie, nombreComunEspecie, familia, autoctona, descripcion, ecologia):
        self.__nombreCientificoEspecie = nombreCientificoEspecie
        self.__nombreComunEspecie = nombreComunEspecie
        self.__familia = familia
        self.__autoctona = autoctona
        self.__descripcion = descripcion
        self.__ecologia = ecologia

    def getNombreFamilia(self):
        return self.__nombreCientificoEspecie

    def setNombreCientificoEspecie(self, nombreCientificoEspecie):
        self.__nombreCientificoEspecie = nombreCientificoEspecie

    def getNombreComunEspecie(self):
        return self.__nombreComunEspecie

    def setNombreComunEspecie(self, nombreComunEspecie):
        self.__nombreComunEspecie = nombreComunEspecie

    def getFamilia(self):
        return self.__familia

    def setFamilia(self, familia):
        self.__familia = familia

    def getAutoctona(self):
        return self.__autoctona

    def setAutoctona(self, autoctona):
        self.__autoctona = autoctona

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getEcologia(self):
        return self.__ecologia

    def setEcologia(self, ecologia):
        self.__ecologia = ecologia

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

# Creación de un nuevo registro usando el constructor del modelo.
#a_record = Especie(nombreComunEspecie="Ciruelo Rojo")
# Guardar el objeto en la base de datos.
#a_record.save()

class Individuos(models.Model):
    nombreComun = models.ForeignKey(Especie, on_delete=models.CASCADE, blank=False)
    motivoSingular = models.CharField('Motivo de Singularidad',choices=motivo_singularidad, blank=False, max_length=30)
    explicacionMotivoSingular = models.CharField('Explicacion',blank=False, max_length=30,default='')
    x = models.IntegerField('X',blank=False, default=1)
    y = models.IntegerField('Y',blank=False,default=1)
    fotoArbol = models.ImageField(upload_to='static/imagenes',blank=False)
    fotoHojas = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoTronco = models.ImageField(upload_to='static/imagenes',blank=True)
    fotoFrutos = models.ImageField(upload_to='static/imagenes',blank=True)
    altura = models.IntegerField('Altura',blank=False, default=1)
    perimetro = models.IntegerField('Perimetro',blank=False, default=1)

    def __str__(self):
            return self.nombreComunEspecie

    def __init__(self, nombreComun, motivoSingular, explicacionMotivoSingular, x, y, altura, perimetro):
        self.__nombreComun = nombreComun
        self.__motivoSingular = motivoSingular
        self.__explicacionMotivoSingular = explicacionMotivoSingular
        self.__x = x
        self.__y = y
        self.__altura = altura
        self.__perimetro = perimetro

    def getNombreComun(self):
        return self.nombreComun

    def setNombreCientificoEspecie(self, nombreComun):
        self.__nombreComun = nombreComun

    def getMotivoSingular(self):
        return self.motivoSingular

    def setMotivoSingular(self, motivoSingular):
        self.__motivoSingular = motivoSingular

    def getExplicacionMotivoSingular(self):
        return self.explicacionMotivoSingular

    def setMotivoSingular(self, explicacionMotivoSingular):
        self.__explicacionMotivoSingular = explicacionMotivoSingular

    def getX(self):
        return self.x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.__y = y

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.__altura = altura

    def getPerimetro(self):
        return self.perimetro

    def setPerimetro(self, perimetro):
        self.__perimetro = perimetro

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

permisos=(('Administrador','Administrador'), ('Usuario','Usuario'),)

class Usuario(models.Model):
    nombreUsuario = models.CharField('Nombre',blank=False,max_length=30,unique=True)
    primerApellido = models.CharField('Primer Apellido',blank=False,max_length=30)
    segundoApellido = models.CharField('Segundo Apellido',blank=False,max_length=30)
    email = models.EmailField('E-mail',blank=False,unique=True)
    contrasenia = models.CharField('Contraseña',blank=False,max_length=30)
    tipo = models.CharField('Tipo',blank=False,choices=permisos,max_length=30, default='Usuario')

    def __str__(self):
            return self.nombreUsuario

    #def encriptarContrasenia(self):
    #    byte[] bytes = System.Text.Encoding.UTF8.GetBytes(self.contrasenia);
    #    SHA256 mySHA256 = SHA256.Create();
    #    bytes = mySHA256.ComputeHash(bytes);
    #    return (System.Text.Encoding.ASCII.GetString(bytes));

    def permisosAdmin(self):
        usuario = list()
        for i in range (self.tipo):
            if self.tipo == Administrador:
                usuario.append(i)
        return usuario

#private string Encriptar(string _contraseña)
#        {
#            byte[] bytes = System.Text.Encoding.UTF8.GetBytes(_contraseña);
#            SHA256 mySHA256 = SHA256.Create();
#            bytes = mySHA256.ComputeHash(bytes);
#            return (System.Text.Encoding.ASCII.GetString(bytes));
#        }
