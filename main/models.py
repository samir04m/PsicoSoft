from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numeroTarjetaProfesional = models.CharField(max_length=50)
    firma = models.ImageField(upload_to="firmas", null=True, blank=True)

class Diagnostico(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre)

class Paciente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipoDocumento = models.CharField(max_length=20)
    numeroDocumento = models.CharField(max_length=20)
    fechaNacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=20, null=True, blank=True)
    estadoCivil = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    nivelEducativo = models.CharField(max_length=50, null=True, blank=True)
    ocupacion = models.CharField(max_length=50, null=True, blank=True)
    motivoConsulta = models.TextField(null=True, blank=True)
    antecedentesPersonales = models.TextField(null=True, blank=True)
    antecedentesFamiliares = models.TextField(null=True, blank=True)
    antecedentesSociales = models.TextField(null=True, blank=True)
    historiaPersonal = models.TextField(null=True, blank=True)
    impresionDiagnostica = models.TextField(null=True, blank=True)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True, blank=True)
    analisis = models.TextField(null=True, blank=True)
    planTrabajo = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField()
    
    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

class Evolucion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField()

class ExceptionLog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    excepcion = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return "{} {}".format(self.descripcion, self.fecha)