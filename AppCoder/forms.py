from django import forms

class CrearCurso(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
    
class CrearEstudiante(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()

class CrearProfesor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class CrearEntregable(forms.Form):
    nombre = forms.CharField(max_length=20)
    Fecha_entrega = forms.DateField(widget=forms.SelectDateWidget)
    entregado = forms.BooleanField(required=False)
        










