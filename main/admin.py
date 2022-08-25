from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

class PsicologoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ('id','usuario',)

class DiagnosticoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre',)

class PacienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['numeroDocumento','nombres','apellidos']
    list_display = ('id','tipoDocumento','numeroDocumento','nombres','apellidos','usuario',)

class EvolucionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['paciente']
    list_display = ('id','paciente','fecha',)

class ExceptionLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ('id','usuario','descripcion','fecha',)

admin.site.register(Psicologo, PsicologoAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Evolucion, EvolucionAdmin)
admin.site.register(ExceptionLog, ExceptionLogAdmin)
