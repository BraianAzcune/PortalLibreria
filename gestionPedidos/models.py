from django.db import models
from django.conf import settings

class Libros(models.Model):
    titulo= models.CharField(max_length=50)
    autor = models.ForeignKey('Autores', on_delete=models.SET_NULL, null=True)
    isbn= models.CharField(max_length=13)

    def __str__(self):
        return "titulo: %s | autor: %s"%(self.titulo, self.autor)


class Autores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)

    def __str__(self):
        return "nombre y apellido: %s %s"%(self.nombre, self.apellido)


class LibroInstancias(models.Model):
    libro = models.ForeignKey('Libros', on_delete=models.SET_NULL, null=True)
    editorial=models.CharField(max_length=50)
    fecha_devolucion = models.DateField(null=True, blank=True)
    cliente= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    biblioteca= models.ForeignKey("Bibliotecas",on_delete=models.SET_NULL,null=True, blank=True)

    ESTADO = (
        ('D', 'Disponible'),
        ('N', 'No disponible'),
    )

    estado = models.CharField(
    max_length=1,
    choices=ESTADO,
    blank=True,
    default='D',
    help_text='Disponiblidad')


class Bibliotecas(models.Model):
    nombre = models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    telefono= models.CharField(max_length=7)

    def __str__(self):
        return "nombre: %s | telefono: %s | direccion: %s"%(self.nombre, self.telefono, self.direccion)