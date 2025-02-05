from inicio.views import inicio, saludo
# from .views import inicio

from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo')
]