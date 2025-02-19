from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAuto, ModificarAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


def inicio(request):
    # return {'clave': 'valor'}
    # return HttpResponse("{'clave': 'valor'}")
    # return HttpResponse("<h1>Hola soy la vista!</h1>")

    return render(request, 'inicio/inicio.html')

def saludo(request, nombre, apellido):
    hora_actual = datetime.now()
    return render(request, 'inicio/saludo.html', {'hora': hora_actual, 'nombre': nombre, 'apellido': apellido})

def crear_auto(request):
    print(request.GET)
    print(request.POST)
    
    formulario = CrearAuto()
    
    if request.method == "POST":
        formulario = CrearAuto(request.POST)
        if formulario.is_valid():
            marca = formulario.cleaned_data.get('marca')
            modelo = formulario.cleaned_data.get('modelo')
            descripcion =formulario.cleaned_data.get('descripcion')
            
            auto = Auto(marca=marca, modelo=modelo, descripcion=descripcion)
            auto.save()
            
            return redirect("listado_de_autos")
    
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

def listado_de_autos(request):
    autos = Auto.objects.all()
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data.get('modelo')
        marca_a_buscar = formulario.cleaned_data.get('marca')
        autos = Auto.objects.filter(modelo__icontains=modelo_a_buscar, marca__icontains=marca_a_buscar)
        
    return render(request, 'inicio/listado_de_autos.html', {'autos': autos, 'formulario': formulario})

def ver_auto(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render(request, 'inicio/ver_auto.html', {'auto': auto})

# Vistas Comunes
def eliminar_auto(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    auto.delete()
    return redirect('listado_de_autos')
    
def modificar_auto(request, auto_id):
    
    auto = Auto.objects.get(id=auto_id)
    
    if request.method == "POST":
        formulario = ModificarAuto(request.POST, instance=auto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_de_autos')
    else:
        formulario = ModificarAuto(instance=auto)
    
    return render(request, 'inicio/modificar_auto.html', {'formulario': formulario})

# CBV
class ModificarAutoVista(UpdateView):
    model = Auto
    template_name = "inicio/CBV/modificar_auto.html"
    fields = "__all__"
    success_url = reverse_lazy('listado_de_autos')

class EliminarAutoVista(DeleteView):
    model = Auto
    template_name = "inicio/CBV/eliminar_auto.html"
    success_url = reverse_lazy('listado_de_autos')
