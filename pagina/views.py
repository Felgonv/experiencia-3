from django.shortcuts import render, redirect
from pagina.models import Producto1
from pagina.Carrito import Carrito
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')

def nosotros(request):
    return render(request, 'nosotros.html')



def contacto(request):
    return render(request, 'contacto.html')

def trabajo(request):
    return render(request, 'trabajo.html')

def Producto(request):
    productos=Producto1.objects.all()
    return render(request, 'Producto.html',{'productos':productos})

def agregar_productos(request,producto_id):
    carrito=Carrito(request)
    producto=Producto1.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Producto")
def eliminar_producto(request,producto_id):
    carrito=Carrito(request)
    producto=Producto1.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Producto")
def restar_producto(request,producto_id):
    carrito=Carrito(request)
    producto=Producto1.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Producto")
def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("Producto")


def salir(request):
    logout(request)
    return redirect('/')