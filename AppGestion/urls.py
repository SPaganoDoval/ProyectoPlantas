from django.urls import path
from AppGestion.views import ProductoListView, insertarProducto,eliminarProducto,editarProducto
#from . import views

urlpatterns = [
    #path('', name= 'producto') ,
    path('', ProductoListView.as_view(), name= 'verProducto') ,  
    path('insertarProducto/', insertarProducto, name= 'insertarProducto'),
    path('eliminarProducto/<int:prod_no>', eliminarProducto, name= 'eliminarProducto'),  
    path('editarProducto/<int:prod_no>', editarProducto, name= 'editarProducto'),
    #path('verProducto/<int:prod_no>/', views.editarProducto, name='editarProducto'),
]



