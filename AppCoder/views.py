from django.shortcuts import render


def Inicio(request):
    return render(request,"index.html")


def Estudiante(request):
    return render(request,"pagina/estudiantes.html")