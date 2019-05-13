from django.db import models
#import crypt


familias=( ('Aceráceas','Aceráceas'), ('Anacardiáceas','Anacardiáceas'), ('Aquifoliáceas','Aquifoliáceas'), ('Betuláceas','Betuláceas'), ('Buxáceas','Buxáceas'), ('Caprifoliáceas','Caprifoliáceas'),('Celastráceas','Celastráceas'),('Cornáceas','Cornáceas'),('Cupresáceas','Cupresáceas'),('Eleagnáceas','Eleagnáceas'),('Ericácas','Ericácas'),('Fagáceas','Fagáceas'),('Juglandáceas','Juglandáceas'),('Lauráceas','Lauráceas'),('Leguminosas','Leguminosas'),('Meliáceas','Meliáceas'),('Mirtáceas','Mirtáceas'),('Moráceas','Moráceas'),('Oleáceas','Oleáceas'),('Palmáceas','Palmáceas'),('Pináceas','Pináceas'),('Platanáceas','Platanáceas'),('Punicáceas','Punicáceas'),('Ramnáceas','Ramnáceas'),('Rosáceas','Rosáceas'),('Salicáceas','Salicáceas'),('Simaroubáceas','Simaroubáceas'),('Solanáceas','Solanáceas'),('Tamariacáceas','Tamariacáceas'),('Taxáceas','Taxáceas'),('Tiliáceas','Tiliáceas'),('Ulmáceas','Ulmáceas'),)

motivo_singularidad=( ('Antigüedad','Antigüedad'), ('Elevado Diámetro','Elevado Diámetro'), ('Plantado por un personaje histórico','Plantado por un personaje histórico'),)

distribucion_predominante=( ('Asia','Asia'), ('Antártida','Antártida'), ('Europa','Europa'), ('África','África'), ('Oceanía','Oceanía'), ('América','América'),)

class Familia(models.Model):
    nombre = models.CharField('Nombre',unique=True,choices=familias, max_length=30,blank=False)

    def __str__(self):
        return self.nombre

    def devolverFamilia(self):
        familias = list()
        for i in range (self.nombre):
            familias.append(i)
            #print(familias)
        return familias

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

    def devolverEspeciePorNombreCientifico(self):
        especies = list()
        for i in range (self.nombreCientifico):
            especies.append(i)
        return especies

    def devolverEspeciePorNombreComun(self):
        especies = list()
        for i in range (self.nombreComun):
            especies.append(i)
        return especies

    def devolverEspeciePorAutoctona(self):
        especies = list()
        for i in range (self.autoctona):
            if self.autoctona == True:
                especies.append(i)
        return especies


class Individuos(models.Model):
    nombre = models.CharField('Nombre',unique=True,blank=False,max_length=30)
    motivoSingular = models.CharField('Motivo de Singularidad',choices=motivo_singularidad, blank=False, max_length=30)
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

    def devolverIndividuoPorNombre(self):
        individuo = list()
        for i in range (self.nombre):
            individuo.append(i)
        return individuo

    def devolverIndividuoPorMotivoSingular(self):
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
    nombre = models.CharField('Nombre',blank=False,max_length=30,unique=True)
    primerApellido = models.CharField('Primer Apellido',blank=False,max_length=30)
    segundoApellido = models.CharField('Segundo Apellido',blank=False,max_length=30)
    email = models.EmailField('E-mail',blank=False,unique=True)
    contrasenia = models.CharField('Contraseña',blank=False,max_length=30)
    tipo = models.CharField('Tipo',blank=False,choices=permisos,max_length=30, default='Usuario')

    def __str__(self):
            return self.nombre

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
