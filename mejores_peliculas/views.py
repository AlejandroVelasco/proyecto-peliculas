from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "mejores_peliculas/index.html")

def detalle(request, id):    
    return render(request, "mejores_peliculas/detalle.html")