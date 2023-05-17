from django.contrib import admin
from django.urls import path
from . import views

#se agregan los endpoints y la vista correspondiente
# para listar y crear productos y proveedores
urlpatterns = [
    path('productos/listado/',views.lista_productos),
    path('productos/crear/',views.agregar_producto,name='agregar-producto'),

    path('proveedores/listado/',views.lista_proveedores),
    path('proveedores/crear/',views.agregar_proveedor,name='agregar-proveedor'),
    path('',views.menu)

]
