from django.urls import path
from AppCoder import views

urlpatterns = [
    path('AppCoder/', views.Inicio, name="Inicio"),
    path('estudiantes/', views.AgregarEstudiante, name="Estudiantes"),
    path('profesores/', views.AgregarProfesor, name="Profesores"),
    path('entregable/', views.AgregarEntregable, name="Entregable"),
    path('entregable/lista/', views.lista_entregables, name="VerEntregables"),
    path('cursos/', views.CursoFormulario, name="Cursos"),
    path('vercursos/', views.VerCursos, name="VerCursos"),
    
    
]
