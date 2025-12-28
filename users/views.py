from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.urls import reverse_lazy
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

from users.models import Avatar
from .forms import AvatarForm, UserRegisterForm, UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin





def login_request(request):
    msg_login = ""

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect("Inicio")   
            else:
                msg_login = "Usuario o contraseña incorrectos"
        else:
            msg_login = "Usuario o contraseña incorrectos"
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register_request(request):
    msg_register = ""

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Inicio")
        else:
            msg_register = "Error al registrar. Revisá los datos."
    else:
        form = UserRegisterForm()

    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})

def logout_request(request):
    logout(request)
    return render(request, "users/logout.html")

  

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.avatar)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AvatarForm(instance=request.user.avatar)
    return render(request, 'avatar.html', {'form': form})



@login_required
def editar_perfil(request):
    usuario = request.user

    # --- Formularios ---
    form = UserEditForm(instance=usuario)

    # Si el usuario ya tiene avatar, lo obtenemos. De lo contrario avatar = None
    avatar = Avatar.objects.filter(user=usuario).first()

    if avatar:
        avatar_form = AvatarForm(instance=avatar)
    else:
        avatar_form = AvatarForm()

    # --- Procesar POST ---
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)

        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        # Validar ambos formularios
        if form.is_valid() and avatar_form.is_valid():
            form.save()

            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = usuario
            avatar_instance.save()

            return redirect("editar_perfil")

    context = {
        "form": form,
        "avatar_form": avatar_form,
    }

    return render(request, "users/editar_usuario.html", context)


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "editar_clave.html"
    success_url = reverse_lazy("editar_perfil")

