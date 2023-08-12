from django import forms

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=256)
    subtitulo = forms.CharField
    cuerpo = forms.CharField(required=True)
    autor = forms.CharField(required=True)
    fecha = forms.DateField(required=True)
    imagen = forms.ImageField