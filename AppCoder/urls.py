from django.urls import path
from AppCoder import views

urlpatterns = [
    path('AppCoder/', views.Inicio, name="Inicio"),
    path('estudiantes/', views.Estudiantes, name="Estudiantes"),
    path('profesores/', views.Profesores, name="Profesores"),
    path('entregable/', views.Entregable, name="Entregable"),
    path('cursos/', views.CursoFormulario, name="Cursos"),
    
]
