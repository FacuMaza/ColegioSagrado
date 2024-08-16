from django import forms
from .models import *

#FORMULARIO PARA LA CARGA DE CURSOS
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        widgets = { 
            'color': forms.Select(choices=[
                ('azul', 'Azul'),
                ('rojo', 'Rojo'),
                ('blanco', 'Blanco'),
            ])
        }


#FORMULARIO PARA LA CARGA DE MATERIAS
class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['descripcion']


# FORMULARIO PARA docentes
class DocentesForm(forms.ModelForm):
    class Meta:
        model = Docentes
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoriaprofesores.objects.all()
        self.fields['nivel'].queryset = Nivelprofesores.objects.all()



# FORMULARIO CARGAR EL TIPO DE SEXO
class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['descripcion']

# FORMULARIO PARA CARGAR EL TIPO DE NECIONALIDAD

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = ['descripcion']


# FORMULARIO PARA CARGAR EL TIPO DE LOCALIDAD

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = ['descripcion']


# FORMULARIO PARA CARGAR EL TIPO DE CASAS
class CasasForm(forms.ModelForm):
    class Meta:
        model = Casas
        fields = ['descripcion']

# FORMULARIO PARA CARGAR EL TIPO DE COLEGIOS
class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegio
        fields = ['descripcion']

# FORMULARIO PARA CARGAR CATEGORIAS PROFESORES
class CategoriasProfesoresForm(forms.ModelForm):
    class Meta:
        model = Categoriaprofesores
        fields = ['descripcion']

# FORMULARIO PARA CARGAR NIVEL PROFESORES
class NivelProfesoresForm(forms.ModelForm):
    class Meta:
        model = Nivelprofesores
        fields = ['descripcion']


# FORMS DEL MODEL FAMILIAS
class FamiliasForm(forms.ModelForm):
    class Meta:
        model = Familias  # Ahora el modelo es Familias
        fields = '__all__'
        exclude = ['fecha_creacion', 'fecha_modificacion']

        widgets = {
            'nombre_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'apellido_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'dni_padre': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'domicilio_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'domicilio_laboral_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'telofono_fijo': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'celular_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'ocupacion_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'email_papa': forms.EmailInput(attrs={'class': 'form-control col-md-4'}),
            'nombre_mama': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'apellido_mama': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'dni_mama': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'domicilio_mama': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'domicilio_laboral_papa': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'celular_mama': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'telofono_fijo': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'ocupacion_mama': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'email_mama': forms.EmailInput(attrs={'class': 'form-control col-md-4'}),
        }

        labels = {
            'nombre_papa': 'Nombre del Padre',
            'apellido_papa': 'Apellido del Padre',
            'dni_padre': 'DNI del Padre',
            'domicilio_papa': 'Domicilio del Padre',
            'domicilio_laboral_papa': 'Domicilio Laboral del Padre',
            'telofono_fijo': 'Teléfono Fijo',
            'celular_papa': 'Celular del Padre',
            'ocupacion_papa': 'Ocupación del Padre',
            'email_papa': 'Correo Electrónico del Padre',
            'nombre_mama': 'Nombre de la Madre',
            'apellido_mama': 'Apellido de la Madre',
            'dni_mama': 'DNI de la Madre',
            'domicilio_mama': 'Domicilio de la Madre',
            'domicilio_laboral_papa': 'Domicilio Laboral de la Madre',
            'celular_mama': 'Celular de la Madre',
            'telofono_fijo': 'Teléfono Fijo',
            'ocupacion_mama': 'Ocupación de la Madre',
            'email_mama': 'Correo Electrónico de la Madre',
        }
        

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'  # Incluye todos los campos
        exclude = ['fecha_creacion', 'fecha_modificacion']
       

        widgets = {
            'id_familia': forms.Select(attrs={'class': 'form-select col-md-4'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'DNI': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'Correo_Electronico_Particular': forms.EmailInput(attrs={'class': 'form-control col-md-4'}),
            'Correo_Electronico_Institucional': forms.EmailInput(attrs={'class': 'form-control col-md-4'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'Localidad': forms.Select(attrs={'class': 'form-select col-md-4'}),
            'Nacionalidad': forms.Select(attrs={'class': 'form-select col-md-4'}),
            'Colegio': forms.Select(attrs={'class': 'form-select col-md-4'}),
            'Sexo': forms.Select(attrs={'class': 'form-select col-md-4'}),
            'Fecha_de_Nacimiento': forms.DateInput(attrs={'class': 'form-control col-md-4', 'type': 'date'}),
            'Lugar_de_nacimiento': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'Casas': forms.Select(attrs={'class': 'form-select col-md-4'}),
            'estado_dispositivos': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
        }

        labels = {
            'id_familia': 'Apellido de la Familia',
            'Correo_Electronico_Particular': 'Correo Electrónico Particular',
            'Correo_Electronico_Institucional': 'Correo Electrónico Institucional',
            'Fecha_de_Nacimiento': 'Fecha de Nacimiento',
            'Lugar_de_nacimiento': 'Lugar de Nacimiento',
        }

class CursoMateriaForm(forms.ModelForm):
    class Meta:
        model = CursoMateria
        fields = '__all__'

    docentes = forms.ModelChoiceField(
        queryset=Docentes.objects.all(),
        label="Docentes",
    )

#FORMS DE NOTAS
class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = [
            'trimestre',
            'PROCESO',
            'PARTICIPACION_EN_CLASE',
            'TP_INDIVIDUAL_1',
            'TP_INDIVIDUAL_2',
            'LECCION_ORAL_INDIVIDUAL',
            'EXPOSICION_ORAL_INDIVIDUAL',
            'EVALUACION_ESCRITA',
            'EXPOSICION1_GRUPAL_NOTA_GRUPAL',
            'EXPOSICION1_GRUPAL_NOTA_INDIVIDUAL',
            'EXPOSICION1_GRUPAL_SOPORTE_PRESENTACION',
            'EXPOSICION2_GRUPAL_NOTA_GRUPAL',
            'EXPOSICION2_GRUPAL_NOTA_INDIVIDUAL',
            'EXPOSICION2_GRUPAL_SOPORTE_PRESENTACION',
            'LABORATORIO_Y_TALLER',
            'CARPETA',
            'MATERIAL',
            'CONDUCTA',
        ]


class MateriaAlumnoForm(forms.ModelForm):
    class Meta:
        model = MateriaAlumno
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define querysets para los campos ForeignKey
        self.fields['cursomateria'] = forms.ModelChoiceField(queryset=CursoMateria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['matricula'] = forms.ModelChoiceField(queryset=Matriculas.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matriculas
        fields = ['id_alumno_matricula', 'curso_matricula']