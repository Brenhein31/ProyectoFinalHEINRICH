from django.contrib import admin
from django.urls import path
from web_blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
]
