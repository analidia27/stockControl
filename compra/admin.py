from django.contrib import admin
from .models import Producto, Proveedor
# Register your models here.


#agrego modelos visibles en el admin
admin.site.register(Producto)
admin.site.register(Proveedor)
