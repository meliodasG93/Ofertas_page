from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html')


def perecible(request):
    return render(request, 'perecible.html')


def Noperecible(request):
    return render(request, 'Noperecible.html')


def Mpuntos(request):
    return render(request, 'Mpuntos.html')

def Registro(request):
    return render(request, 'registro.html')

def Tiendas(request):
    return render(request, 'tiendas.html')

def aProducto(request):
    return render(request, 'aProducto.html')

def login(request):
    return render(request, 'login.html')