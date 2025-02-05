from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def inicio(request):
    # return {'clave': 'valor'}
    # return HttpResponse("{'clave': 'valor'}")
    # return HttpResponse("<h1>Hola soy la vista!</h1>")

    return render(request, 'inicio/inicio.html')

def saludo(request, nombre, apellido):
    hora_actual = datetime.now()
    return render(request, 'inicio/saludo.html', {'hora': hora_actual, 'nombre': nombre, 'apellido': apellido})