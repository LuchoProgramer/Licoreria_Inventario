from django import forms
from .models import Venta, VentaProducto

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['metodo_pago', 'sucursal', 'usuario']

class VentaProductoForm(forms.ModelForm):
    class Meta:
        model = VentaProducto
        fields = ['producto', 'cantidad', 'precio_unitario']
