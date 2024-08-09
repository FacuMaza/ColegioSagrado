from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.auth.models import User
from .forms import AlumnosForm, CasasForm, CategoriasProfesoresForm, ColegioForm, CursoForm, CursoMateriaForm, DocentesForm, FamiliasForm, LocalidadForm, MateriaAlumnoForm,MateriaForm, MatriculaForm, NacionalidadForm, NivelProfesoresForm, NotasForm, SexoForm


def index(request):
    return render(request, "index.html")

def alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})

def docentes(request):
    docentes = Docentes.objects.all()
    context = {
        'docentes': docentes,
    }
    return render(request, "docentes.html",context)

def familias(request):
    familia = Familias.objects.all()
    return render(request, "familias.html", {'familia': familia})

def cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos,
    }
    return render(request, 'cursos.html', context)

# DETALLES CURSOS
def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id_curso=curso_id)
    materias = CursoMateria.objects.filter(curso=curso)
    context = {
        'curso': curso,
        'materias': materias,
        'curso_id': curso.id_curso
    }
    return render(request, 'detallecursos.html', context)

def materias(request):
    materia = Materia.objects.all()
    context = {
        'materia': materia,
    }
    return render(request, 'materias.html', context)
    

def configuracion(request):
    return render(request, "configuracion.html")

def LogoutPage(request):
    logout(request)
    return redirect('index')

#FUNCION PARA PERMITIR EL INGRESO DEL USUARIO
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)#vERIFICA LA EXISTENCIA DEL USUARIO INGRESADO
        if user is not None: #SI EL USUARIO EXISTE
            login(request,user)
            request.session['username'] = username

            # Obtener el rol del usuario
            try:
                rol = UsuarioRol.objects.get(usuario=user).rol
            except UsuarioRol.DoesNotExist:
                rol = "Sin Rol"

            # Pasar el rol y el username a la sesión
            request.session['rol'] = rol
            request.session['username'] = username # Asegúrate de que el nombre de usuario esté disponible en la sesión

            return redirect('home')
        else:
            return HttpResponse ("Usuario y Contraseña incorrectos!!!")
    return render (request,'login.html')

@login_required(login_url='login')
def HomePage(request):
    username = request.session.get('username', None)
    if username:
        context = {'username': username}
        return render(request, 'home.html', context)
    else:
        error_message = "Debe iniciar sesión primero...!"
        return render(request, 'error.html', {'error_message': error_message})



# VIWS PARA CARGAR CURSOS
# Opción 1: Usando una vista de función
def anadircurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    return render(request, 'anadircursos.html', {'form': form})




# VIWS PARA CARGAR MATERIAS
def anadirmateria(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MateriaForm()
    return render(request, 'anadirmaterias.html', {'form': form})

# VIWS PARA CARGAR DOCENTES
def anadirdocentes(request):
    if request.method == 'POST':
        form = DocentesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DocentesForm()
    return render(request, 'anadirdocentes.html', {'form': form})

# VIWS PARA CARGAR SEXO
def anadirsexo(request):
    if request.method == 'POST':
        form = SexoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SexoForm()
    return render(request, 'anadirsexo.html', {'form': form})

# VIWS PARA CARGAR NACIONALIDAD
def anadirnacionalidad(request):
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NacionalidadForm()
    return render(request, 'anadirnacionalidad.html', {'form': form})


# VIWS PARA CARGAR LOCALIDAD
def anadirlocalidad(request):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LocalidadForm()
    return render(request, 'anadirlocalidad.html', {'form': form})


# VIWS PARA CARGAR CASAS
def anadircasas(request):
    if request.method == 'POST':
        form = CasasForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CasasForm()
    return render(request, 'anadircasas.html', {'form': form})

# VIWS PARA CARGAR COLEGIO
def anadircolegio(request):
    if request.method == 'POST':
        form = ColegioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ColegioForm()
    return render(request, 'anadircolegios.html', {'form': form})


# VIWS PARA CARGAR ALUMNOS
def anadiralumno(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            alumno_nuevo = form.save()
            
            return redirect('mostraralumnofamilia', id_alumno=alumno_nuevo.id_alumno)
    else:
        form = AlumnosForm()
    return render(request, 'anadiralumno.html', {'form': form})
# VIWS PARA LA MUESTRA DE ALUMNOS
def mostraralumnofamilia(request, id_alumno):
    alumno = get_object_or_404(Alumnos, pk=id_alumno)
    familia = alumno.id_familia

    context = {
        'alumno': alumno,
        'familia': familia
    }
    return render(request, 'mostraralumnofamilia.html', context)





# VIWS PARA CARGAR ALUMNOS
def anadirmatriculas(request, alumno_id):
    alumno = get_object_or_404(Alumnos, id=alumno_id)
    matricula = get_object_or_404(Matriculas, id_alumno=alumno)
    return render(request, 'anadirmatriculas.html', {'alumno': alumno, 'matricula': matricula})



# VIWS PARA VER MATRICULAS
def ver_matriculas(request, id_alumno):
    alumno = get_object_or_404(Alumnos, pk=id_alumno)
    matriculas = Matriculas.objects.filter(id_alumno=alumno) # Utiliza la relación ForeignKey 
    context = {
        'alumno': alumno,
        'matriculas': matriculas,
    }
    return render(request, 'matriculas.html', context)

# VIWS cargar MATRICULAS
def crear_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a una página de éxito
    else:
        form = MatriculaForm()
    return render(request, 'crear_matricula.html', {'form': form})


# VIWS PARA CARGAR FAMILIAS
def anadirfamilias(request):
    if request.method == 'POST':
        form = FamiliasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anadiralumno')  # Redirige a la misma vista
    else:
        form = FamiliasForm()
    return render(request, 'anadirfamilias.html', {'form': form})


# VIWS PARA VER DATOS DE FAMILIAS
def detallefamilias(request,familia_id):
    familias = Familias.objects.get(pk=familia_id) 
    return render(request, 'detallefamilias.html', {'familias': familias})




# VIWS PARA CARGAR CATEGORIAS PROFESORES
def anadircategoriasdocente(request):
    if request.method == 'POST':
        form = CategoriasProfesoresForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriasProfesoresForm()
    return render(request, 'anadircagoriasdocentes.html', {'form': form})

# VIWS PARA CARGAR NIVEL PROFESORES
def anadirniveldocente(request):
    if request.method == 'POST':
        form = NivelProfesoresForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NivelProfesoresForm()
    return render(request, 'anadirnivelprofesores.html', {'form': form})


# VIWS PARA CARGAR Usuarios y CREAR UN REGISTRO CON EL ROL DE ESE USUARIO
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        rol = request.POST.get('rol')

        # Validación de entrada (opcional pero recomendada)
        if not uname or not email or not pass1 or not rol:
            error_message = "Por favor, llena todos los campos."
            return render(request, 'registrarusuario.html', {'error_message': error_message})

        if User.objects.filter(username=uname).exists():
            error_message = "Ese nombre de usuario ya está en uso."
            return render(request, 'registrarusuario.html', {'error_message': error_message})
        
        try:
            # Crea el usuario con hash de contraseña
            my_user = User.objects.create_user(username=uname, password=pass1, email=email)
            my_user.save()
        
            # Crea el UserProfile para el nuevo usuario
            nuevo_usuario_rol = UsuarioRol(usuario=my_user, rol=rol)  # Usa my_user aquí
            nuevo_usuario_rol.save()
            return redirect('login')  # Redirecciona a la vista de inicio de sesión

        except Exception as e:
            error_message = "Ocurrió un error al crear el usuario. Por favor, intentalo de nuevo."
            return render(request, 'registrarusuario.html', {'error_message': error_message})

    else:
        # Mostrar el formulario de registro
        return render(request, 'registrarusuario.html')


# VIWS PARA CARGAR CURSOS-MATERIAS-DOCENTES
def anadircursomateriasdocente(request):
    if request.method == 'POST':
        form = CursoMateriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoMateriaForm()
    return render(request, 'anadirmaterias.html', {'form': form})



# VIWS PARA CARGAR NOTAS

   
def gestionar_notas(request, curso_materia_id):
    # Obtener la materia del curso según el ID proporcionado
    cursomateria = get_object_or_404(CursoMateria, id=curso_materia_id)

    # Obtener los estudiantes matriculados en el curso asociado a la materia
    estudiantes_en_materia = Matriculas.objects.filter(
        curso_matricula=cursomateria.curso
    ).distinct()

    # Obtener las notas ya existentes para los estudiantes en la materia
    notas_existentes = Notas.objects.filter(
        id_cursomateria=cursomateria,
        id_matricula__in=estudiantes_en_materia
    ).values('id_matricula', 'trimestre')  

    # Crear un diccionario para almacenar las notas (para la vista)
    notas_por_estudiante = {}
    for nota in notas_existentes:
        matricula_id = nota['id_matricula']
        trimestre = nota['trimestre']
        if matricula_id not in notas_por_estudiante:
            notas_por_estudiante[matricula_id] = {}
        notas_por_estudiante[matricula_id][trimestre] = True  

    # Renderizar la plantilla con los datos
    return render(request, 'gestionar_notas.html', {
        'cursomateria': cursomateria,
        'estudiantes_en_materia': estudiantes_en_materia,
        'notas_por_estudiante': notas_por_estudiante,
        'curso_materia_id' : cursomateria.materia,
        'curso': cursomateria.curso,
        'docente': cursomateria.docente,
        
    })


def gestionar_nota(request, curso_materia_id, matricula_id, trimestre):
    cursomateria = get_object_or_404(CursoMateria, id=curso_materia_id)
    matricula = get_object_or_404(Matriculas, id=matricula_id)

    # Busca la Nota si ya existe (para edición)
    try:
        nota = Notas.objects.get(id_cursomateria=cursomateria, id_matricula=matricula, trimestre=trimestre)
    except Notas.DoesNotExist:
        nota = None

    if request.method == 'POST':
        form = NotasForm(request.POST, instance=nota) 
        if form.is_valid():
            nota = form.save()
            return redirect('gestionar_notas', curso_materia_id=cursomateria.id) 
    else:
        form = NotasForm(instance=nota)

    return render(request, 'gestionar_nota.html', {
        'form': form,
        'cursomateria': cursomateria,
        'matricula': matricula,
        'trimestre': trimestre
    })

















def materia_alumno_create(request):
    if request.method == 'POST':
        form = MateriaAlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = MateriaAlumnoForm()
    context = {'form': form}
    return render(request, 'anadirmateriaalumno.html', context)