from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from perfiles.models import *

class UsuarioForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]