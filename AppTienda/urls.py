from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
]