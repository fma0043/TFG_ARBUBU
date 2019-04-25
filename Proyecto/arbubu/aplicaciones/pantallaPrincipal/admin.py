from django.contrib import admin
from .models import Familia, Especie, Individuos
# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'ecologia', 'distribucion', 'id' )
    search_fields = ('nombre', 'descripcion', 'ecologia', 'distribucion')

class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombreEspecie', 'caracteristicas', 'familia', 'id' )
    search_fields = ('nombreEspecie', 'caracteristicas', 'familia')

class IndividuosAdmin(admin.ModelAdmin):
    list_display = ('nombreIndividuos', 'caracteristicas', 'especie', 'id' )
    search_fields = ('nombreIndividuos', 'caracteristicas', 'especie',)

admin.site.register(Familia,FamiliaAdmin)
admin.site.register(Especie,EspecieAdmin)
admin.site.register(Individuos,IndividuosAdmin)
