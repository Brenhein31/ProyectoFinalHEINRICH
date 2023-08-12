from django.contrib import admin
from django.urls import path, include
from web_blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
    path("articulos/", include("blog.urls")),
    path("perfiles/", include("perfiles.urls")),
    path("about/", SobreMiTemplateView.as_view(), name="sobre_mi"),
]