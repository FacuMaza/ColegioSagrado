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
        model = Familias
        fields = '__all__'

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'  # Incluye todos los campos del modelo

        widgets = {
            'id_familia': forms.Select(attrs={'class': 'form-control'}),
            'Fecha_de_Nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_familia'].queryset = Familias.objects.all()



class CursoMateriaForm(forms.ModelForm):
    class Meta:
        model = CursoMateria
        fields = '__all__'

        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }


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