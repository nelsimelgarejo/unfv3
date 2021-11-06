from django.contrib import admin
from .models import Perfil, FichaSociodemografica, ItemsTopicos, ComponenteBienestar, RespuestasPuente, ResultadoPerfil, DataUNFV, Retroalimentacion
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
admin.site.register(Perfil)
admin.site.register(FichaSociodemografica)
admin.site.register(ResultadoPerfil)
admin.site.register(RespuestasPuente)


class ItemsTopicosResource(resources.ModelResource):
    class Meta:
        model = ItemsTopicos

class ItemsTopicosAdmin(ImportExportModelAdmin,admin.ModelAdmin): # new
    search_fields = ['item']
    list_display = ('topico','item','inverso','creado','actualizado','estado',)
    resources_class = ItemsTopicosResource

admin.site.register(ItemsTopicos, ItemsTopicosAdmin)

class ComponenteBienestarResource(resources.ModelResource):
    class Meta:
        model = ComponenteBienestar

class ComponenteBienestarAdmin(ImportExportModelAdmin,admin.ModelAdmin): # new
    search_fields = ['item']
    list_display = ('perfil','topico','completado','estado','creado','actualizado',)
    resources_class = ComponenteBienestarResource

admin.site.register(ComponenteBienestar, ComponenteBienestarAdmin)

class DataUNFVResource(resources.ModelResource):
    class Meta:
        model = DataUNFV

class DataUNFVAdmin(ImportExportModelAdmin,admin.ModelAdmin): # new
    search_fields = ['nombre_completo', 'codigo_estudiante', 'dni']
    list_display = ('facultad','escuela','codigo_estudiante','correo','dni','nombre_completo','creado','activado','estado',)
    resources_class = DataUNFVResource

admin.site.register(DataUNFV, DataUNFVAdmin)


class RetroalimentacionResource(resources.ModelResource):
    class Meta:
        model = Retroalimentacion

class RetroalimentacionAdmin(ImportExportModelAdmin,admin.ModelAdmin): # new
    search_fields = ['topico', 'retro_text','nivel']
    list_display = ('topico', 'retro_text','nivel','creado','estado',)
    resources_class = RetroalimentacionResource

admin.site.register(Retroalimentacion, RetroalimentacionAdmin)
