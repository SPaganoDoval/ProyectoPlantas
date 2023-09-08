from django.shortcuts import render,redirect
from django.views.generic import DetailView
from AppGestion.models import Producto
from AppCarrito.Carrito import Carrito

# Create your views here.
def tienda(request):
    productos=Producto.objects.all()
    return render(request,'tiendaonline.html',{'productos':productos})

def agregar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.agregar(producto)
    return redirect('tienda')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

class detallar_productoDetailView(DetailView):
    model=Producto
    template_name='detalleProducto.html'
    def get_object(self):
        objeto=self.model.objects.get(id=self.kwargs['pk'])
        return objeto



