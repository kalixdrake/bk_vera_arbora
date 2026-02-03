from django.contrib import admin

from .models import Arbol, Taxonomia, FotoArbol

class FotoArbolInline(admin.TabularInline):
    model = FotoArbol
    extra = 1

@admin.register(Arbol)
class ArbolAdmin(admin.ModelAdmin):
    list_display = ('no_arbol', 'codigo_distrital', 'taxonomia', 'fecha_visita')
    search_fields = ('no_arbol', 'codigo_distrital')
    inlines = [FotoArbolInline]

@admin.register(Taxonomia)
class TaxonomiaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_comun', 'nombre_cientifico')
    search_fields = ('codigo', 'nombre_comun', 'nombre_cientifico')
