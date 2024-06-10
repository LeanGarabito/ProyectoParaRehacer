from django.shortcuts import render, redirect
from .models import *
from .forms import *


def Inicio(request):
    return render(request,'pagina/inicio.html')
  
def CursoFormulario(request):
    if  request.method == 'POST':
        formulario = CrearCurso(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            curso = Curso(
                nombre=datos.get('nombre'),
                camada = datos.get('camada'))
            curso.save()
    formulario = CrearCurso()
    return render(request,"pagina/cursos.html",{'formulario': formulario})
      
def VerCursos(request):
    cursos = Curso.objects.all()
    return render(request,'pagina/vercursos.html',{"cursos":cursos})

def AgregarEstudiante(request):
    if request.method == 'POST':
        formulario = CrearEstudiante(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiante(
                nombre=datos.get('nombre'),
                apellido =datos.get('apellido'),
                email=datos.get('email'))
            estudiante.save()
    formulario = CrearEstudiante()
    return render(request,'pagina/estudiantes.html',{'formulario': formulario})

def AgregarProfesor(request):
    if request.method == 'POST':
        formulario = CrearProfesor(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            profesor = Profesor(
                nombre=datos.get('nombre'),
                apellido =datos.get('apellido'),
                email=datos.get('email'),
                profesion=datos.get('profesion'))
            profesor.save()
    formulario = CrearProfesor()
    return render(request,'pagina/profesores.html',{'formulario': formulario})


# def AgregarEntregable(request):
#     if request.method == 'POST':
#         formulario = CrearEntregable(request.POST)
#         if formulario.is_valid():
#             datos = formulario.cleaned_data
#             entregable = Entregable(nombre=datos.get('nombre'),fechaDeEntrega=datos.get('fechaDeEntrega'), entregado=datos.get('entregado'))
#             entregable.save()
#             return redirect('inicio')  
#     else:
#         formulario = CrearEntregable()
#     return render(request, 'pagina/entregable.html', {'formulario': formulario})
        

def AgregarEntregable(request):
    if request.method == 'POST':
        formulario = CrearEntregable(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            entregable = Entregable(
                nombre=datos.get('nombre'),
                Fecha_entrega=datos.get('Fecha_entrega'),
                entregado=datos.get('entregado')
            )
            entregable.save() 
            return redirect('VerEntregables')
    formulario = CrearEntregable()
    return render(request, 'pagina/entregable.html', {'formulario': formulario})    

def lista_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'pagina/lista_entregables.html', {'entregables': entregables})


            