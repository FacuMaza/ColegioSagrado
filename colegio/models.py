from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# MODELO PARA LA CARGA EL USUARIO CON ROL




# MODELO PARA LA CARGA EL TIPO DE CURSO

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="Azul")

    def __str__(self):
        return f"{self.descripcion} ({self.color})"



# MODELO PARA CARGAR MATERIAS
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

#MODELO PARA CARGAR SEXO
class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, default="M")

    def __str__(self):
        return self.descripcion


#MODELO PARA CARGAR NACIONALIDAD
class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, default="Argentina")
    

    def __str__(self):
        return self.descripcion



#MODELO PARA CARGAR LOCALIDAD
class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, default="Capital")
    

    def __str__(self):
        return self.descripcion
    
#MODELO PARA CARGAR CASAS
class Casas(models.Model):
    id_casas = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    

    def __str__(self):
        return self.descripcion
    
#MODELO PARA CARGAR COLEGIOS
class Colegio(models.Model):
    id_colegio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    

    def __str__(self):
        return self.descripcion


#MODELO PARA CARGAR FAMILIA
class Familias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_papa = models.CharField(max_length=255)
    apellido_papa = models.CharField(max_length=255)
    dni_padre = models.CharField(max_length=255)
    domicilio_papa = models.CharField(max_length=255)
    domicilio_laboral_papa = models.CharField(max_length=255)
    telofono_fijo = models.IntegerField()
    celular_papa = models.CharField(max_length=255)
    ocupacion_papa = models.CharField(max_length=255)
    email_papa = models.CharField(max_length=255)
    nombre_mama = models.CharField(max_length=255)
    apellido_mama = models.CharField(max_length=255)
    dni_mama = models.CharField(max_length=255)
    domicilio_mama = models.CharField(max_length=255)
    domicilio_laboral_papa = models.CharField(max_length=255)
    celular_mama = models.CharField(max_length=255)
    telofono_fijo = models.IntegerField(default='00')
    ocupacion_mama = models.CharField(max_length=255)
    email_mama = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.nombre_papa} - {self.nombre_mama}"

#MODELO PARA CARGAR ALUMNOS
class Alumnos(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    id_familia =models.ForeignKey(Familias, verbose_name='Apellido de la Familia', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=10)
    Correo_Electronico_Particular = models.EmailField(max_length=254, blank=True)
    Correo_Electronico_Institucional = models.EmailField(max_length=254, blank=True)
    Direccion = models.CharField(max_length=100)
    Localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE)
    Nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    Colegio = models.ForeignKey(Colegio,on_delete=models.CASCADE)
    Sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)
    Fecha_de_Nacimiento = models.DateField()
    Lugar_de_nacimiento = models.CharField(max_length=100)
    Casas = models.ForeignKey(Casas,on_delete=models.CASCADE)
    estado_dispositivos = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.Nombre + " " + self.Apellido
    


#MODELO PARA CARGAR CATEGORIAS PROFESORES
class Categoriaprofesores(models.Model):
    id_categorias = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    

    def __str__(self):
        return self.descripcion

#MODELO PARA CARGAR NIVEL PROFESORES
class Nivelprofesores(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    

    def __str__(self):
        return self.descripcion
    
# MODELO PARA CARGAR PROFESORES
class Docentes(models.Model):
    id_docentes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cuil = models.IntegerField()
    legajo_administrativo = models.IntegerField()
    legajo_reloj = models.IntegerField()
    numero_legajo_sueldo = models.IntegerField(default='00')
    horario = models.IntegerField()
    categoria = models.ForeignKey(Categoriaprofesores, verbose_name='Categoria', on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivelprofesores, verbose_name='Nivel', on_delete=models.CASCADE)
    titulo_base = models.CharField(max_length=255)
    fomacion_academica = models.CharField(max_length=255)
    telefono = models.IntegerField(default='00')
    correo_electronico_personal = models.CharField(max_length=255)
    correo_electronico_institucional = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


# MODELO PARA RELACIONAR CURSO MATERIA 

class CursoMateria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docentes, related_name='curso_materias')
    codigo = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.materia}"
    

# MODELO PARA CARGAR MATRICULAS
class Matriculas(models.Model):
    id_alumno_matricula = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    curso_matricula = models.ForeignKey(Curso, on_delete=models.CASCADE, default=4)
    fecha_creacion_matricula = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id_alumno_matricula}"


class Notas(models.Model):
    TRIMESTRES = [
        (1, 'Primer Trimestre'),
        (2, 'Segundo Trimestre'),
        (3, 'Tercer Trimestre'),
    ]
    id_cursomateria = models.ForeignKey(CursoMateria, on_delete=models.CASCADE, default=None)
    id_matricula = models.ForeignKey(Matriculas, on_delete=models.CASCADE)
    trimestre = models.IntegerField(choices=TRIMESTRES)
    PROCESO = models.FloatField(blank=True, null=True)
    PARTICIPACION_EN_CLASE = models.FloatField(blank=True, null=True)
    TP_INDIVIDUAL_1 = models.FloatField(blank=True, null=True)
    TP_INDIVIDUAL_2 = models.FloatField(blank=True, null=True)
    LECCION_ORAL_INDIVIDUAL = models.FloatField(blank=True, null=True)
    EXPOSICION_ORAL_INDIVIDUAL = models.FloatField(blank=True, null=True)
    EVALUACION_ESCRITA = models.FloatField(blank=True, null=True)
    EXPOSICION1_GRUPAL_NOTA_GRUPAL = models.FloatField(blank=True, null=True)
    EXPOSICION1_GRUPAL_NOTA_INDIVIDUAL = models.FloatField(blank=True, null=True)
    EXPOSICION1_GRUPAL_SOPORTE_PRESENTACION = models.FloatField(blank=True, null=True)
    EXPOSICION2_GRUPAL_NOTA_GRUPAL = models.FloatField(blank=True, null=True)
    EXPOSICION2_GRUPAL_NOTA_INDIVIDUAL = models.FloatField(blank=True, null=True)
    EXPOSICION2_GRUPAL_SOPORTE_PRESENTACION = models.FloatField(blank=True, null=True)
    LABORATORIO_Y_TALLER = models.FloatField(blank=True, null=True)
    CARPETA = models.FloatField(blank=True, null=True)
    MATERIAL = models.FloatField(blank=True, null=True)
    CONDUCTA = models.CharField(max_length=50)

    def __str__(self):
        return f"Notas {self.get_trimestre_display()}"




class UsuarioRol(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=100)
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE, null=True, blank=True)  # Nuevo campo

    def __str__(self):
        return self.rol














class MateriaAlumno(models.Model):
    cursomateria = models.ForeignKey(CursoMateria, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matriculas, on_delete=models.CASCADE)