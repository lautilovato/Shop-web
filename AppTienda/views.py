from django.shortcuts import render
from .forms import *
from .models import Zapatilla
    
def inicio(request):
   
    return render(request, "AppTienda/inicio.html")

def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            zapatilla = Zapatilla()
            zapatilla.imagen = form.cleaned_data["imagen"]
            zapatilla.modelo = form.cleaned_data["modelo"]
            zapatilla.marca = form.cleaned_data["marca"]
            zapatilla.save()
            form = ProductoForm()
        else:
            form = ProductoForm()

    return render(request, "AppTienda/agregar_producto.html")

