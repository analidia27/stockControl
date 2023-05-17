from django.shortcuts import redirect, render
from .forms import ProductoForm, ProveedorForm
from .models import Producto, Proveedor


#Lista todos los productos registrados en la base de datos
def lista_productos(request):
    try:
        #almaceno todos los objetos del tipo Producto
        productos = Producto.objects.all()
        #creo diccionario que contenga todos los productos de la bd
        context = {
            'productos': productos
        }
        #renderizo el template de listado de productos con el diccionario creado
        return render(request, 'lista_productos.html',context)
    except Exception:
        #si existe alguna excepcion, renderizo el template de errores
        return render(request, 'errors.html')
    
# Permite agregar un nuevo producto
def agregar_producto(request):
    #crea formulario para Producto
    form = ProductoForm()
    #consulto si la peticion es tipo POST
    if request.method == 'POST':
        #crea formulario para Producto con los datos enviados en POST
        form = ProductoForm(request.POST)
        #si los datos recibidos son validos, creo una instancia de la clase Producto
        if form.is_valid():
            producto = Producto(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                stock_actual = form.cleaned_data['stock_actual'],
                proveedor = form.cleaned_data['proveedor']
            )
            #guardo la instancia
            producto.save()
            #redirecciono a la vista de listado, para que muestre todos los productos existentes hasta este momento
            return redirect('../listado/')
        else:
            return redirect('../listado/')
    #creo diccionario 
    context = { 'form': form } 
    #renderiza la plantilla junto con el diccionario enviado
    return render(request, '/agregar_producto.html',context)

#Lista todos los productos creados en la Base de datos
def lista_proveedores(request):
    try:
        proveedores = Proveedor.objects.all().order_by('id')
        context = {
            'proveedores': proveedores
        }
        return render(request, 'lista_proveedores.html',context)

    except Exception:
        return render(request, 'errors.html')

#Permite agregar un nuevo proveedor.
def agregar_proveedor(request):
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        print(form)
        if form.is_valid():
            producto = Proveedor(
                razon_social = form.cleaned_data['razon_social'],
                cuit = form.cleaned_data['cuit'],
                celular = form.cleaned_data['celular'],
            )
            producto.save()
            return redirect('../listado/')
        else:
            return redirect('../listado/')

    context = { 'form': form } 
    return render(request, 'agregar_proveedor.html',context)


def menu(request):
    return render(request, 'compras.html')
