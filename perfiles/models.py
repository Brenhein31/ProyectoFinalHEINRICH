from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class Consulta(models.Model):
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    detalle = models.TextField(blank=True)