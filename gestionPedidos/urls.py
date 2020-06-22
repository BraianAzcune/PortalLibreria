from django.urls import path
from . import views

urlpatterns = [
    path("",views.misLibros),
    path("mislibros/",views.misLibros, name="misLibros"),
    path("buscarLibro/",views.buscarLibro, name="buscarLibro"),
    path("guardarReserva/",views.guardarReserva,name="guardarReserva"),
]