from inicio.views import inicio, saludo, crear_auto, listado_de_autos
# from .views import inicio

from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear-auto/', crear_auto, name='crear_auto'),
    path('listado-de-autos/', listado_de_autos, name='listado_de_autos'),
]