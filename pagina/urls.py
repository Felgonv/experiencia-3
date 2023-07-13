from django.urls import path
from .views import  agregar_productos, eliminar_producto, index, galeria, limpiar_carrito, nosotros, contacto, Producto, restar_producto, trabajo, salir

urlpatterns = [
    path('', index,name="index"),
    path('galeria/', galeria,name="galeria"),
    path('contacto/', contacto,name="contacto"),
    path('trabajo/', trabajo,name="trabajo"),
    path('Producto/', Producto,name="Producto"),
    path('nosotros/', nosotros,name="nosotros"),
    path('agregar/<int:producto_id>/', agregar_productos,name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto,name="Del"),
    path('restar/<int:producto_id>/', restar_producto,name="Sub"),
    path('limpiar/', limpiar_carrito,name="CLS"),
    path('salir/', salir, name="salir")
]