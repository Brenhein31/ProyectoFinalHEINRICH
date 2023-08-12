from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from blog.models import *

class ArticuloListView(ListView):
    model = Articulo
    template_name = "blog/articulo_lista.html"

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy("ver_articulo")

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = "__all__"
    success_url = reverse_lazy("lista_articulos")

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = "__all__"
    success_url = reverse_lazy("lista_articulos")

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
   model = Articulo
   success_url = reverse_lazy("lista_articulos")

