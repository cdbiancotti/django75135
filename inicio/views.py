from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAuto


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