# Generated by Django 4.1 on 2022-11-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_psicologo_firma_remove_psicologo_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
