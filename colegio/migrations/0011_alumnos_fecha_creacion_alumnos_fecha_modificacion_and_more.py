# Generated by Django 5.0.7 on 2024-08-01 15:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0010_auto_20240801_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='fecha_modificacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='familias',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='familias',
            name='fecha_modificacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='matriculas',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
