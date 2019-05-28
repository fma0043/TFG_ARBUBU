from django.contrib import admin
from .models import Familia, Especie, Individuos, Usuario
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','nombreFamilia')
    search_fields = ('nombreFamilia','id')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id','nombreCientificoEspecie', 'nombreComunEspecie',  'autoctona', 'descripcion', 'ecologia')
    search_fields = ('id','nombreCientificoEspecie', 'nombreComunEspecie', )

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'id','nombreComun','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'id','nombreComun','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nombreUsuario','primerApellido','segundoApellido','email','contrasenia','tipo')
    search_fields = ('id','nombreUsuario','primerApellido','segundoApellido','email','tipo')



admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
admin.site.register(Usuario,UsuarioAdmin)
