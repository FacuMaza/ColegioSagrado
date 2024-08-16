# Generated by Django 5.0.7 on 2024-08-15 23:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriaprofesores',
            fields=[
                ('id_categorias', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(default='Capital', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nivelprofesores',
            fields=[
                ('id_nivel', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='familias',
            old_name='telefono_mama',
            new_name='domicilio_laboral_papa',
        ),
        migrations.RenameField(
            model_name='familias',
            old_name='id_familia',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='familias',
            name='telefono_papa',
        ),
        migrations.AddField(
            model_name='curso',
            name='color',
            field=models.CharField(default='Azul', max_length=7),
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
            model_name='familias',
            name='telofono_fijo',
            field=models.IntegerField(default='00'),
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id_docentes', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('cuil', models.IntegerField()),
                ('legajo_administrativo', models.IntegerField()),
                ('legajo_reloj', models.IntegerField()),
                ('numero_legajo_sueldo', models.IntegerField(default='00')),
                ('horario', models.IntegerField()),
                ('titulo_base', models.CharField(max_length=255)),
                ('fomacion_academica', models.CharField(max_length=255)),
                ('telefono', models.IntegerField(default='00')),
                ('correo_electronico_personal', models.CharField(max_length=255)),
                ('correo_electronico_institucional', models.CharField(max_length=255)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.categoriaprofesores', verbose_name='Categoria')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.nivelprofesores', verbose_name='Nivel')),
            ],
        ),
        migrations.CreateModel(
            name='CursoMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.materia')),
                ('docentes', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='colegio.docentes')),
            ],
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('DNI', models.CharField(max_length=10)),
                ('Correo_Electronico_Particular', models.EmailField(blank=True, max_length=254)),
                ('Correo_Electronico_Institucional', models.EmailField(blank=True, max_length=254)),
                ('Direccion', models.CharField(max_length=100)),
                ('Fecha_de_Nacimiento', models.DateField()),
                ('Lugar_de_nacimiento', models.CharField(max_length=100)),
                ('estado_dispositivos', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_modificacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('Casas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.casas')),
                ('Colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.colegio')),
                ('Nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.nacionalidad')),
                ('Sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.sexo')),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.familias', verbose_name='Apellido de la Familia')),
                ('Localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.localidad')),
            ],
        ),
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_matricula', models.DateTimeField(default=django.utils.timezone.now)),
                ('curso_matricula', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
                ('id_alumno_matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cursomateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.cursomateria')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.matriculas')),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.IntegerField(choices=[(1, 'Primer Trimestre'), (2, 'Segundo Trimestre'), (3, 'Tercer Trimestre')])),
                ('PROCESO', models.FloatField(blank=True, null=True)),
                ('PARTICIPACION_EN_CLASE', models.FloatField(blank=True, null=True)),
                ('TP_INDIVIDUAL_1', models.FloatField(blank=True, null=True)),
                ('TP_INDIVIDUAL_2', models.FloatField(blank=True, null=True)),
                ('LECCION_ORAL_INDIVIDUAL', models.FloatField(blank=True, null=True)),
                ('EXPOSICION_ORAL_INDIVIDUAL', models.FloatField(blank=True, null=True)),
                ('EVALUACION_ESCRITA', models.FloatField(blank=True, null=True)),
                ('EXPOSICION1_GRUPAL_NOTA_GRUPAL', models.FloatField(blank=True, null=True)),
                ('EXPOSICION1_GRUPAL_NOTA_INDIVIDUAL', models.FloatField(blank=True, null=True)),
                ('EXPOSICION1_GRUPAL_SOPORTE_PRESENTACION', models.FloatField(blank=True, null=True)),
                ('EXPOSICION2_GRUPAL_NOTA_GRUPAL', models.FloatField(blank=True, null=True)),
                ('EXPOSICION2_GRUPAL_NOTA_INDIVIDUAL', models.FloatField(blank=True, null=True)),
                ('EXPOSICION2_GRUPAL_SOPORTE_PRESENTACION', models.FloatField(blank=True, null=True)),
                ('LABORATORIO_Y_TALLER', models.FloatField(blank=True, null=True)),
                ('CARPETA', models.FloatField(blank=True, null=True)),
                ('MATERIAL', models.FloatField(blank=True, null=True)),
                ('CONDUCTA', models.CharField(max_length=50)),
                ('id_cursomateria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='colegio.cursomateria')),
                ('id_matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.matriculas')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioRol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=100)),
                ('docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.docentes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
