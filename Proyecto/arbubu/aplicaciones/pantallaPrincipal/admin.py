from django.contrib import admin
from .models import Familias, Especies, Individuos, Usuario
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombreFamilia',)
    search_fields = ('nombreFamilia',)

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombreCientificoEspecie', 'nombreComunEspecie',  'autoctona', 'descripcion', 'ecologia')
    search_fields = ('nombreCientificoEspecie', 'nombreComunEspecie', )

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombreUsuario','primerApellido','segundoApellido','email','contrasenia','tipo')
    search_fields = ('nombreUsuario','primerApellido','segundoApellido','email','tipo')



admin.site.register(Familias,FamiliaAdmin)
admin.site.register(Especies,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
admin.site.register(Usuario,UsuarioAdmin)
