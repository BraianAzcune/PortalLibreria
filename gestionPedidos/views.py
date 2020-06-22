from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def misLibros(request):
    
    
    
    return render(request,"gestion/misLibros.html")



def buscarLibro(request):
    pass

