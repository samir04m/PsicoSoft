# Generated by Django 4.1 on 2022-08-25 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroTarjetaProfesional', models.CharField(max_length=50)),
                ('firma', models.ImageField(blank=True, null=True, upload_to='firmas')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('tipoDocumento', models.CharField(max_length=20)),
                ('numeroDocumento', models.CharField(max_length=20)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=20, null=True)),
                ('estadoCivil', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('nivelEducativo', models.CharField(blank=True, max_length=50, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=50, null=True)),
                ('motivoConsulta', models.TextField(blank=True, null=True)),
                ('antecedentesPersonales', models.TextField(blank=True, null=True)),
                ('antecedentesFamiliares', models.TextField(blank=True, null=True)),
                ('antecedentesSociales', models.TextField(blank=True, null=True)),
                ('historiaPersonal', models.TextField(blank=True, null=True)),
                ('impresionDiagnostica', models.TextField(blank=True, null=True)),
                ('analisis', models.TextField(blank=True, null=True)),
                ('planTrabajo', models.TextField(blank=True, null=True)),
                ('fecha', models.DateTimeField()),
                ('diagnostico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.diagnostico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExceptionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('excepcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.paciente')),
            ],
        ),
    ]
