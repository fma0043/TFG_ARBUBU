from django.contrib import admin
from .models import Familia, Especie, Individuos, Usuario
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombreCientifico', 'nombreComun', 'familia', 'autoctona', 'distribucion', 'descripcion', 'ecologia', 'masInfo' )
    search_fields = ('nombreCientifico', 'nombreComun', 'familia')

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'nombre','motivoSingular','x','y','tipoEspecie','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'nombre','motivoSingular','x','y','tipoEspecie','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','primerApellido','segundoApellido','email','contrasenia','tipo')
    search_fields = ('nombre','primerApellido','segundoApellido','email','tipo')



admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
admin.site.register(Usuario,UsuarioAdmin)
