from django import forms
from .models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'ubicacion']  # Incluye aquí todos los campos que deseas manejar en el formulario
