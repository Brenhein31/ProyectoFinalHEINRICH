from django.contrib import admin
from django.urls import path
from perfiles.views import *

urlpatterns = [
    path("contacto/", ConsultaCreateView.as_view(), name="enviar_consulta"),
    path("registro/", UsuarioCreateView.as_view(), name="registro"),
    path("iniciar-sesion/", UsuarioLoginView.as_view(), name="login"),
    path("cerrar-sesion/", UsuarioLogoutView.as_view(), name="logout"),
    path("mi-perfil/", MiPerfilTemplateView.as_view(), name="mi_perfil"),
    path("agregar-avatar/", AvatarCreateView.as_view(), name="agregar_avatar"),
]