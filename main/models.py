from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import base64
# from PIL import Image

class Psicologo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numeroTarjetaProfesional = models.CharField(max_length=50)
    firmaBase64 = models.BinaryField(db_column='firma', null=True, blank=True, editable=True)
    logoBase64 = models.BinaryField(db_column='logo', null=True, blank=True, editable=True)

    def set_firma(self, firma):
        if firma:
            self.firmaBase64 = base64.b64encode(firma.read())
    def get_firma(self):
        if self.firmaBase64:
            firmaDecode = base64.b64decode(self.firmaBase64)
            return base64.b64encode(firmaDecode).decode('utf8')
        return None
    firma = property(get_firma, set_firma)

    def set_logo(self, logo):
        if logo:
            self.logoBase64 = base64.b64encode(logo.read())
    def get_logo(self):
        if self.logoBase64:
            logoDecode = base64.b64decode(self.logoBase64)
            return base64.b64encode(logoDecode).decode('utf8')
        return None
    logo = property(get_logo, set_logo)

    def getImagenFirma(self):
        return "data:image/png;base64, " + str(self.firma)

    def getImagenLogo(self):
        return "data:image/png;base64, " + str(self.logo)

    # firma = models.ImageField(upload_to="firmas", null=True, blank=True)
    # logo = models.ImageField(upload_to="logos", null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     super(Psicologo, self).save(*args, **kwargs)
    #     if self.firma:
    #         image = Image.open(self.firma.path)
    #         image.save(self.firma.path, quality=20, optimize=True)
    #     if self.logo:
    #         image = Image.open(self.logo.path)
    #         image.save(self.logo.path, quality=20, optimize=True)


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