from django.urls import path
from colegio import views

urlpatterns = [
    path('', views.index, name= "index"),
    
    path('login/',views.LoginPage,name="login"), #login
    
    path('home/',views.HomePage,name="home"),#home
    
    path('logout/',views.LogoutPage,name='logout'), #SALIR
        
    path('alumnos/', views.alumnos, name= "alumnos"), #MOSTRARALUMNOS
    path('anadiralumno/', views.anadiralumno, name= "anadiralumno"), #ANADIRALUMNOS
    path('detallealumno/<int:alumno_id>/', views.detallealumno, name='detallealumno'),




    path('profesores/', views.profesores, name= "docentes"), #DOCENTES
    path('anadirdocentes/', views.anadirdocentes, name= "anadirdocentes"), #ANADIR DOCENTES
    path('catogirasdocentes/', views.anadircategoriasdocente, name= "categoriasdocentes"), #CATEGORIAS DOCENTES
    path('niveldocentes/', views.anadirniveldocente, name= "niveldocentes"), #NIVEL DOCENTES


    path('familias/', views.familias, name= "familias"), #MOSTRARFAMILIAS
    path('anadirfamilia/', views.anadirfamilias, name= "anadirfamilia"), #ANADIRFAMILIAS
    path('detallefamilia/<int:familia_id>/', views.detallefamilias, name='detallefamilia'),



    path('cursos/', views.cursos, name= "cursos"),#MOSTRARCURSOS
    path('anadircurso/', views.anadircurso, name= "anadircurso"), #ANADIRCURSOS
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'), #DETALLE DE CURSOS



    path('configuracion/', views.configuracion, name= "configuracion"),


    path('materias/', views.materias, name= "materias"), #MOSTRARMATERIAS
    path('anadirmateria/', views.anadirmateria, name= "anadirmateria"), #ANADIRMATERIAS
    

    path('sexo/', views.anadirsexo, name= "anadirsexo"),# ANADIRSEXO

    path('nacionalidad/', views.anadirnacionalidad, name= "anadirnacionalidad"),# ANADIRNACIONALIDAD

    path('localidad/', views.anadirlocalidad, name= "anadirlocalidad"),# ANADIRLOCALIDAD

    path('casas/', views.anadircasas, name= "anadircasas"),# ANADIRCASAS

    path('colegio/', views.anadircolegio, name= "anadircolegio"),# ANADIRCOLEGIO


    path('registro/', views.SignupPage, name= "registro"),# ANADIRCOLEGIO



    path('anadirmatriculas/<int:id_alumno>/', views.anadirmatriculas, name= "anadirmatriculas"),# generar matriculas
    path('ver_matriculas/<int:id_alumno>/', views.ver_matriculas, name='ver_matriculas'), # VER MATRICULAS


    path('cursomateria/', views.anadircursomateriasdocente, name= "cursomateria"),# ANADIR CURSO MATERIAS DOCENTES



    
    
]

