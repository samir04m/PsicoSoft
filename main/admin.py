from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Diagnostico)
admin.site.register(Paciente)
admin.site.register(Evolucion)
admin.site.register(ExceptionLog)
