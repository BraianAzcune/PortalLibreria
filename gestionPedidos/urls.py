from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("mislibros/",views.misLibros, name="misLibros"),
    path("buscarLibro/",views.buscarLibro, name="buscarLibro"),
    path("guardarReserva/",views.guardarReserva,name="guardarReserva"),
    path("catalogo/",views.catalogo,name="catalogo"),
    path("registrarDevolucion/",views.registrarDevolucion,name="registrarDevolucion"),
    path("sinPermisos/",views.sinPermisos,name="sinPermisos"),
]