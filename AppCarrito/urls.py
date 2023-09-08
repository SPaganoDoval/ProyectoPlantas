from django.urls import path
from AppCarrito.views import tienda,agregar_producto, sacar_producto, limpiar_carrito,detallar_productoDetailView 

urlpatterns = [
    path('',tienda,name='tienda'),
    path('agregar/<int:prod_id>',agregar_producto,name='Agregar'),
    path('sacar/<int:prod_id>',sacar_producto,name='Sacar'),
    path('limpiar/',limpiar_carrito,name='Limpiar'),
    path('detalleProducto/<pk>',detallar_productoDetailView.as_view(), name='detalleProducto')
]