from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path("entradas/", ArticuloListView.as_view(), name="lista_articulos"),
    path("entradas/<int:pk>/", ArticuloDetailView.as_view(), name="ver_articulo"),
    path("crear-articulo/", ArticuloCreateView.as_view(), name="crear_articulo"),
    path("editar-articulo/<int:pk>/", ArticuloUpdateView.as_view(), name="editar_articulo"),
    path("eliminar-articulo/<int:pk>/", EstudianteDeleteView.as_view(), name="eliminar_articulo"),
]