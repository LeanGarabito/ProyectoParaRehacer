from django.urls import path
from AppCoder import views

urlpatterns = [
    path('AppCoder/', views.Inicio, name="Inicio"),
    path('estudiantes/', views.AgregarEstudiante, name="Estudiantes"),
    path('profesores/', views.AgregarProfesor, name="Profesores"),
    path('entregable/', views.agregar_entregable, name="Entregable"),
    path('cursos/', views.CursoFormulario, name="Cursos"),
    path('vercursos/', views.VerCursos, name="VerCursos"),
    
    
]
