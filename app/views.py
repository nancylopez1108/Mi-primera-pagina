from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Medico, Paciente, Turnos
from .forms import MedicosFormulario, PacientesFormulario, TurnosFormulario
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse





def inicio(request):
    return render(request, "inicio.html")

def Pacientes(request):
    return render(request, "Pacientes.html")

def About(request):
    return render(request, "About.html")

def Medicos(request):
    lista_medicos = Medico.objects.all()
    return render(request, "Medicos.html", {"medicos": lista_medicos})

@login_required
def turnos(request):
    return render(request, "Turnos.html")

@login_required
def turnosFormulario(request):
    if request.method == "POST":
        miFormulario = TurnosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            turno = Turnos(
                nombre = informacion["nombre"],
                dni_paciente = informacion["dni_paciente"],
                fecha = informacion["fecha"],
                hora = informacion["hora"],
                especialidad = informacion["especialidad"] )
            turno.save()
            return render(request, "inicio.html")
    else:
        miFormulario = TurnosFormulario()

    return render(request, "turnosFormulario.html", {"miFormulario": miFormulario})




def pacientesFormulario(request):
    if request.method == "POST":
        miFormulario = PacientesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            paciente = Paciente( nombre=informacion["nombre"],apellido=informacion["apellido"],DNI=informacion["dni_paciente"],   
                email=informacion["email"])

            paciente.save()
            return render(request, "inicio.html")
    else:
        miFormulario = PacientesFormulario()
    return render(request, "pacientesFormulario.html", {"miFormulario": miFormulario})
@login_required
def busquedaTurno(request):
    return render(request, "busquedaTurno.html")

def buscar(request):
    dni = request.GET.get("dni")

    if dni:
        turnos = Turnos.objects.filter(dni_paciente=dni)
        return render(request,"resultadosTurnos.html", {"turnos": turnos, "dni": dni})
    return HttpResponse("No enviaste DNI")

def medicosFormulario(request):
    if request.method == "POST":
        miFormulario = MedicosFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            medico = Medico(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                especialidad=informacion["especialidad"],
                email=informacion["email"])
            medico.save()
            return render(request, "inicio.html")
    else:
        miFormulario = MedicosFormulario()

    return render(request, "medicosFormulario.html", {"miFormulario": miFormulario})

class MedicoListView(ListView):
        model = Medico
        template_name = "Medicos.html"
        context_object_name = "medicos"

class MedicoDetailView(DetailView):
    model = Medico
    template_name = "MedicoDetail.html"
    context_object_name = "medico"

class MedicoCreateView(LoginRequiredMixin,CreateView):
    model = Medico
    fields = ["nombre", "apellido","email", "especialidad"]
    template_name = "Medico-Create.html"
    success_url = reverse_lazy ("Medicos")

class MedicoUpdateView(LoginRequiredMixin,UpdateView):
    model = Medico
    fields = ["email", "especialidad"]
    template_name = "Medico_Update.html"
    success_url = reverse_lazy("Medicos")

class MedicoDeleteView(LoginRequiredMixin,DeleteView):
    model = Medico
    template_name = "Medico-Delete.html"
    success_url = reverse_lazy ("Medicos")


def Servicios(request):
    
    Servicios = [
        {"nombre": "Clínica Médica",
         "descripcion": "Atención integral para adultos, controles de salud y diagnósticos generales.",
         "imagen": "servicios/clinica_medica.jpg",
         "url": reverse("turnosFormulario")
        },
        {
            "nombre": "Nutrición",
            "descripcion": "Asesoramiento nutricional,personalizado y enfocado a tus necesidades.",
            "imagen": "servicios/nutricion.jpg",
            "url": reverse("turnosFormulario")
        },
        {
            "nombre": "Oftalmología",
            "descripcion": "Controles de la vista, tratamientos y cirugias oculares.",
            "imagen": "servicios/oftalmologia.jpg",
            "url": reverse("turnosFormulario")
        }
    ]
    return render(request, "servicios.html", {"servicios": Servicios})