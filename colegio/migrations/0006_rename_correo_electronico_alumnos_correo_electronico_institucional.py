# Generated by Django 5.0.7 on 2024-07-30 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0005_remove_docentes_celular_mama_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumnos',
            old_name='Correo_Electronico',
            new_name='Correo_Electronico_institucional',
        ),
    ]
