from django.contrib import admin
from .models import Familia, Genero, Especie, Individuos
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class FamiliaResource(resources.ModelResource):
   class Meta:
     model = Familia

class GeneroResource(resources.ModelResource):
   class Meta:
     model = Genero

class EspecieResource(resources.ModelResource):
   class Meta:
     model = Especie

class IndividuoResource(resources.ModelResource):
   class Meta:
     model = Individuos

class FamiliaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('idFamilia','nombreFamilia')
    search_fields = ('idFamilia','nombreFamilia')
    resources_class = FamiliaResource

class GeneroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('idGenero','nombreGenero','familia')
    search_fields = ('idGenero','nombreGenero','familia')
    resources_class = GeneroResource

class EspecieAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('idEspecie','nombreCientificoEspecie', 'nombreComunEspecie', 'genero', 'autoctona', 'descripcion', 'ecologia')
    search_fields = ('idEspecie','nombreCientificoEspecie', 'nombreComunEspecie', 'genero')
    resources_class = EspecieResource

class IndividuosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ( 'idIndividuo','nombreComun','especie','motivoSingular','explicacionMotivoSingular','latitud','longitud','fotoArbol','fotoHojas','fotoTronco','fotoFrutos','ubicacion','altura','perimetro' )
    search_fields = ( 'idIndividuo','nombreComun','especie','motivoSingular','explicacionMotivoSingular','latitud','longitud','ubicacion')
    resources_class = IndividuoResource

admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Genero,GeneroAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
