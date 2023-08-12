from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

class SobreMiTemplateView(TemplateView):
    template_name = "sobre_mi.html"