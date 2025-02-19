from inicio.views import inicio, saludo, crear_auto, listado_de_autos, ver_auto, modificar_auto, eliminar_auto, ModificarAutoVista, EliminarAutoVista
# from .views import inicio

from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear-auto/', crear_auto, name='crear_auto'),
    path('listado-de-autos/', listado_de_autos, name='listado_de_autos'),
    path('ver-auto/<int:auto_id>/', ver_auto, name='ver_auto'),
    # Vistas comunes
    # path('modificar-auto/<int:auto_id>/', modificar_auto, name='modificar_auto'),
    # path('eliminar-auto/<int:auto_id>/', eliminar_auto, name='eliminar_auto'),
    # CBV
    path('modificar-auto/<int:pk>/', ModificarAutoVista.as_view(), name='modificar_auto'),
    path('eliminar-auto/<int:pk>/', EliminarAutoVista.as_view(), name='eliminar_auto'),
]