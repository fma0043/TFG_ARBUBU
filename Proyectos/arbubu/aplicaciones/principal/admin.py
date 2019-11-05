from django.contrib import admin
from .models import Familia, Genero, Especie, Individuos

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('idFamilia','nombreFamilia')
    search_fields = ('idFamilia','nombreFamilia')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('idGenero','nombreGenero','familia')
    search_fields = ('idGenero','nombreGenero','familia')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('idEspecie','nombreCientificoEspecie', 'nombreComunEspecie', 'genero', 'autoctona', 'descripcion', 'ecologia')
    search_fields = ('idEspecie','nombreCientificoEspecie', 'nombreComunEspecie', 'genero')

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ( 'idIndividuo','nombreComun','especie','motivoSingular','explicacionMotivoSingular','x','y','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','altura','perimetro' )
    search_fields = ( 'idIndividuo','nombreComun','especie','motivoSingular','explicacionMotivoSingular','x','y')


admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Genero,GeneroAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
