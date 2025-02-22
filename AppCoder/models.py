from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    Fecha_entrega = models.DateField()
    entregado = models.BooleanField(default=False)
    def __str__(self):
        return f"Nombre: {self.nombre}\nFecha de envio: {self.Fecha_entrega}\nEntrega: {self.entregado}"