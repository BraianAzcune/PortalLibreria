from django.contrib import admin
from gestionPedidos.models import Libros, Autores, Bibliotecas, LibroInstancias
# Register your models here.
admin.site.register(Libros)
admin.site.register(Autores)
admin.site.register(Bibliotecas)
admin.site.register(LibroInstancias)