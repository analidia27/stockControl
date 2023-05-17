from django.db import models

# Modelo para proveedor con atributos razon_social, cuit y celular. Todos son obligatorioas
class Proveedor(models.Model):
    razon_social = models.CharField(max_length=50)
    cuit = models.IntegerField()
    celular = models.IntegerField()

    def __str__(self):
        return f"{self.razon_social}"

# Modelo para producto con atributos nombre, precio, stock_actual y proveedor que hace referencia a un Proveedor previamente creado
#Todos son obligatorioas
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.nombre} {self.precio} {self.stock_actual}"

