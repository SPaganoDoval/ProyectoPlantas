from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.db import models 
from django.shortcuts import render,redirect
from AppGestion.models import Producto
from django.views.generic import ListView






# AppGestion

#def inicio(request):
    #return render(request,'inicio.html')

class ProductoListView(ListView):
    model=Producto
    template_name= 'productos.html'
    def get_queryset(self):
        return Producto.objects.all()


def insertarProducto(request):
    var_id=request.POST['id']
    var_nombre=request.POST['nombre']
    var_imagen1=request.POST['imagen1']
    var_precio=request.POST['precio']
    producto=Producto.objects.create(id=var_id,
                                     nombre=var_nombre,
                                     imagen1=var_imagen1,
                                     precio=var_precio)
    return redirect('verProducto')

'''def editarProducto(request,prod_no):
    producto=Producto(id=prod_no)
    producto.nombre="Calendula"
    producto.imagen1= "calendulas.jpg"
    producto.precio=40
    producto.save()
    return redirect('verProducto')'''


def editarProducto(request, prod_no):
#def editarProducto(request, pk):
    producto = Producto.objects.get(id=prod_no)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.imagen1 = request.POST['imagen1']
        producto.precio = request.POST['precio']
        producto.save()
   
        return redirect('verProducto')
    return render(request, 'editarProducto.html', {'producto': producto})

def eliminarProducto(request,prod_no):
    producto=Producto.objects.get(id=prod_no)
    producto.delete()
    return redirect('verProducto')