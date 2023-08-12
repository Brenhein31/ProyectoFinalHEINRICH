from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField(blank=True)
    autor = models.CharField(max_length=256)
    fecha = models.DateField(null=True)
    imagen = models.ImageField