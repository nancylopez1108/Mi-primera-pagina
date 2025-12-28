from django import forms 
from django import forms

class TurnosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    dni_paciente = forms.IntegerField()
    fecha = forms.DateField()
    hora = forms.TimeField()
    especialidad = forms.CharField(max_length=50)

class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni_paciente = forms.IntegerField()
    email = forms.EmailField()

class MedicosFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=30)

