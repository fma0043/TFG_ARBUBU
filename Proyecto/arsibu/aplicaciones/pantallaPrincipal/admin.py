from django.contrib import admin
from .models import Familia, Especie, Individuos, Usuario
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('idFamilia','nombreFamilia')
    search_fields = ('nombreFamilia','idFamilia')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('idEspecie','nombreCientificoEspecie', 'nombreComunEspecie', 'familia', 'autoctona', 'descripcion', 'ecologia')
    search_fields = ('idEspecie','nombreCientificoEspecie', 'nombreComunEspecie', )

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'idIndividuo','nombreComun','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'idIndividuo','nombreComun','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('idUsuario','nombreUsuario','primerApellido','segundoApellido','email','contrasenia','tipo')
    search_fields = ('idUsuario','nombreUsuario','primerApellido','segundoApellido','email','tipo')



admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
admin.site.register(Usuario,UsuarioAdmin)
