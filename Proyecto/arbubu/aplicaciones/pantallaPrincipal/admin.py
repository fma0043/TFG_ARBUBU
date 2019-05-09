from django.contrib import admin
from .models import Familia, Especie, Individuos, Usuario
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre','id')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id','nombreCientifico', 'nombreComun', 'familia', 'autoctona', 'distribucion', 'descripcion', 'ecologia', 'masInfo' )
    search_fields = ('nombreCientifico', 'nombreComun', 'familia')

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'id','nombre','motivoSingular','x','y','tipoEspecie','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'nombre','motivoSingular','x','y','tipoEspecie','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')



admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
admin.site.register(Usuario,UsuarioAdmin)
