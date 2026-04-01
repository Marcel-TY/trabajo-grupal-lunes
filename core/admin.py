from django.contrib import admin
from .models import Docente, Ramo, Informe

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['cod_doc', 'nombre', 'especialidad']

@admin.register(Ramo)
class RamoAdmin(admin.ModelAdmin):
    list_display = ['id_ramo', 'descripcion']

@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):
    list_display = ['folio', 'nom_alu', 'docente', 'ramo', 'nota_final', 'estado']
