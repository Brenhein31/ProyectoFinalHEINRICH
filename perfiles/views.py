from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from perfiles.forms import *
from perfiles.models import *

class ConsultaCreateView(CreateView):
    model = Consulta
    fields = "__all__"
    template_name = "perfiles/consulta_crear.html"
    success_url = reverse_lazy("inicio")

class UsuarioCreateView(CreateView):
    form_class = UsuarioForm
    template_name = "perfiles/registro.html"
    success_url = reverse_lazy("mi_perfil")

class UsuarioLoginView(LoginView):
    template_name = "perfiles/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("mi_perfil")

class UsuarioLogoutView(LogoutView):
    template_name = 'perfiles/logout.html'

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = "__all__"
    success_url = reverse_lazy("mi_perfil")

class AvatarCreateView(LoginRequiredMixin, CreateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("inicio")

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("inicio")

class AvatarDeleteView(LoginRequiredMixin, DeleteView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("inicio")

class MiPerfilTemplateView(LoginRequiredMixin, TemplateView):
   template_name = 'perfiles/mi_perfil.html'