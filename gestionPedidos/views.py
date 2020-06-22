from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gestionPedidos.models import LibroInstancias, Libros
from datetime import date, timedelta

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
    

    if request.method == 'POST':

        busqueda= request.POST["busqueda"]
        
        queryset = Libros.objects.filter(titulo__icontains=busqueda)
        lista= list()
        for libro in queryset:
            lista.append(libro.libroInstancia.all())

        #print(lista)

        #librosInstancias= LibroInstancias.objects.libro.get(nombre=busqueda)
        #print("________________________________________________________________")
        #print(librosInstancias)
        #print(queryset)


        return render(request,"gestion/buscarLibros.html",{"lista":lista})
    else:

        return render(request, "gestion/buscarLibros.html")


@login_required
def guardarReserva(request):

    if request.method == 'POST':
        libro= request.POST["libro"]
        #es del tipo gestionPedidos.models.LibroInstancias
        instancia= LibroInstancias.objects.filter(id=libro)[0]
        instancia.estado="N"
        instancia.fecha_devolucion= date.today() +timedelta(15)
        user= request.user._wrapped if hasattr(request.user,'_wrapped') else request.user
        instancia.cliente= user
        instancia.save()

    return redirect('misLibros')