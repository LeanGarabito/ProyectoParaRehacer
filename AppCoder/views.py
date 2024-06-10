from django.shortcuts import render
from .models import *
from AppCoder.forms import CrearCurso,CrearEstudiante,CrearProfesor,CrearEntregable


def Inicio(request):
    return render(request,'pagina/inicio.html')

def Estudiantes(request):
    return render(request,'pagina/estudiantes.html')

# def Entregable(request):
    # return render(request, 'pagina/entregable.html')

def Profesores(request):
    return render(request,'pagina/profesores.html')

# def Cursos(request):
    # return render(request,'pagina/cursos.html')
    
    
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
                mail=datos.get('mail'))
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
                mail=datos.get('mail'),
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
        

def agregar_entregable(request):
    if request.method == 'POST':
        formulario = CrearEntregable(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            entregable = Entregable(
                nombre=datos.get('nombre'),
                fechaDeEntrega=datos.get('fechaDeEntrega'),
                entregado=datos.get('entregado')
            )
            entregable.save()
            return redirect('lista_entregables')  # Redirige a una vista de lista de entregables o una página de éxito
    else:
        formulario = CrearEntregable()
    return render(request, 'pagina/entregable.html', {'formulario': formulario})    

def lista_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'pagina/lista_entregables.html', {'entregables': entregables})

            