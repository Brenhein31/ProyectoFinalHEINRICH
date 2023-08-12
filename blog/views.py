from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import *
from blog.forms import *

class ArticuloListView(ListView):
    model = Articulo
    template_name = "blog/lista_articulos.html"

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy("lista_articulos")

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ("titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen")
    success_url = reverse_lazy("lista_articulos")

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ("titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen")
    success_url = reverse_lazy("lista_articulos")

class ArticuloDeleteView(DeleteView):
   model = Articulo
   success_url = reverse_lazy('lista_articulos')

