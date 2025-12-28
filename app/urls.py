
from django.urls import path
from app import views
from .views import MedicoCreateView, MedicoDeleteView, MedicoListView, MedicoDetailView,MedicoUpdateView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    #path('Medicos/', views.Medicos, name="Medicos"),
    path('Turnos/', views.turnos, name="Turnos"),
    path('Pacientes/', views.Pacientes, name="Pacientes"),
    path('turnosFormulario/', views.turnosFormulario, name="turnosFormulario"),
    path("pacientesFormulario/", views.pacientesFormulario, name="pacientesFormulario"),
    path("busquedaTurno/", views.busquedaTurno, name="busquedaTurno"),
    path("buscar/", views.buscar, name="buscar"),
    path("medicosFormulario/", views.medicosFormulario, name="medicosFormulario"),
    path("medicosFormulario/", views.medicosFormulario, name="medicosFormulario"),
    path("Medicos/", MedicoListView.as_view(), name="Medicos"),
    path("Medicos/<int:pk>/", MedicoDetailView.as_view(), name="Medicos-detail"),
    path("Medicos/create/", MedicoCreateView.as_view(), name="Medicos-Create"),
    path("Medicos/create/", MedicoCreateView.as_view(), name="Medicos-Create"),
    path("Medicos/modifica/<int:pk>", MedicoUpdateView.as_view(), name="Medicos-Update"),
    path("Medicos/elimina/<int:pk>", MedicoDeleteView.as_view(), name="Medicos-Delete"),
    path('About/', views.About, name="About"),
    path("servicios/", views.Servicios, name="servicios"),
]

