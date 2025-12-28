from django.db import models

# Create your models here.

from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    especialidad = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    DNI = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Turnos(models.Model):
    nombre = models.CharField(max_length=30)              
    dni_paciente = models.IntegerField()                  
    fecha = models.DateField()                            
    hora = models.TimeField()                             
    especialidad = models.CharField(max_length=50)  
