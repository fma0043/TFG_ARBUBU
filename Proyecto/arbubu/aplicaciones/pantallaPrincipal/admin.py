from django.contrib import admin
from .models import Familia, Especie, Individuos, Usuario
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombreFamilia',)
    search_fields = ('nombreFamilia',)

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombreCientificoEspecie', 'nombreComunEspecie', 'familia', 'autoctona', 'descripcion', 'ecologia')
    search_fields = ('nombreCientificoEspecie', 'nombreComunEspecie', 'familia')

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'nombreComun','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'nombreComun','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombreUsuario','primerApellido','segundoApellido','email','contrasenia','tipo')
    search_fields = ('nombreUsuario','primerApellido','segundoApellido','email','tipo')



admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
admin.site.register(Usuario,UsuarioAdmin)
