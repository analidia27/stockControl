from django import forms
from .models import Producto,Proveedor

#clase base para agregar la clase form-contro a cada input
class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-6'
            
#formulario de Producto, incluye todos los atributos
class ProductoForm(BaseForm):
    class Meta:
        model = Producto
        fields = '__all__'


#formulario de Proveedor, incluye todos los atributos
class ProveedorForm(BaseForm):
    class Meta:
        model = Proveedor
        fields = '__all__'