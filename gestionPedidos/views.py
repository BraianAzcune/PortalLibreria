from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestionPedidos.models import LibroInstancias


@login_required
def misLibros(request):
    
    #no seas perezoso y traenos los datos. 
    #django tiene clases perezoas, de esta forma le exigimos que la info.
    user= request.user._wrapped if hasattr(request.user,'_wrapped') else request.user

    #obtenemos todos los clientes 
    libros= user.libroInstancia.all()

    print(type(libros))
    #print(libros.objects.all())  
 
#    for libro in libros:
#       print(libro.__dict__())
 #       print(libro.libro.titulo)
      
    
    return render(request,"gestion/misLibros.html",{"libros":libros})


@login_required
def buscarLibro(request):
    pass

