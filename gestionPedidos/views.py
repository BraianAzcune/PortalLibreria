from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from gestionPedidos.models import LibroInstancias, Libros
from datetime import date, timedelta




#redireccionador
@login_required
def inicio(request):
    
    if esBibliotecario(request.user):
        return redirect('catalogo')
    elif esLector(request.user):
        return redirect('misLibros')
    else:
        return render(request,"sinPermiso.html")

def esBibliotecario(user):
    group= getGrupo(user)
    if group.name == "bibliotecas":
        return True
    return False

def esLector(user):
    group= getGrupo(user)
    if group.name =="lectores":
        return True
    return False


def getGrupo(user):
    return  user.groups.filter(user=user)[0] 


def sinPermisos(request):
    return render(request,"sinPermisos.html")
#LADO CLIENTE
@login_required
@user_passes_test(esLector,login_url='sinPermisos')
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
@user_passes_test(esLector,login_url='sinPermisos')
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
@user_passes_test(esLector,login_url='sinPermisos')
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

#LADO BIBLIOTECA

@login_required
@user_passes_test(esBibliotecario,login_url='sinPermisos')
def catalogo(request):

    librosInstancias=request.user.biblioteca.all()[0].libroInstancia.all()

    
    return render(request,"biblioteca/catalogo.html",{"lista":librosInstancias})

@login_required
@user_passes_test(esBibliotecario,login_url='sinPermisos')
def registrarDevolucion(request):


    if request.method=="POST":
        libro= request.POST["libro"]
        instancia= LibroInstancias.objects.filter(id=libro)[0]
        instancia.estado="D"
        instancia.fecha_devolucion= None
        instancia.cliente= None
        instancia.save()
        

    librosInstancias=request.user.biblioteca.all()[0].libroInstancia.filter(estado="N")

    
    return render(request,"biblioteca/registrarDevolucion.html",{"lista":librosInstancias})