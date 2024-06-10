from django import forms

class CrearCurso(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    














# class EstudianteForm(forms.ModelForm):
#     class Meta:
#         model = Estudiante
#         fields = ['nombre','apellido','email']
        

# class ProfesortForm(forms.ModelForm):
#     class meta:
#         model = Profesor
#         fields = ['nombre', 'apellido', 'email', 'profesion']


# class EntregableForm(forms.ModelForm):
#     class Meta:
#         model = Entregable
#         fields = ['nombre', 'fecha_de_entrega', 'entregado']