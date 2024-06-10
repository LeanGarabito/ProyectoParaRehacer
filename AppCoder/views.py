from django.shortcuts import render
from .models import *
from AppCoder.forms import CrearCurso


def Inicio(request):
    return render(request,'pagina/inicio.html')

def Estudiantes(request):
    return render(request,'pagina/estudiantes.html')

def Entregable(request):
    return render(request, 'pagina/entregable.html')

def Profesores(request):
    return render(request,'pagina/profesores.html')

# def Cursos(request):
    # return render(request,'pagina/cursos.html')
    
    
def CursoFormulario(request):
    # if request == "POST":
    #     curso = Curso(request.POST['curso'],request.POST['camada'])
    #     curso.save()
    #     return render(request,'pagina/inicio.html')
    # return render(request,'pagina/cursos.html')
    if  request == "POST":
        ...
    formulario = CrearCurso()
    return render(request,"pagina/cursos.html",{'formulario': formulario})
    