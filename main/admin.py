from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['username','email']
    list_display = ('username','email','is_staff','is_superuser','is_active',)

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


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Psicologo, PsicologoAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Evolucion, EvolucionAdmin)
admin.site.register(ExceptionLog, ExceptionLogAdmin)
