"""licoreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),           # URLs para la aplicación de usuarios
    path('productos/', include('productos.urls')),         # URLs para la aplicación de productos
    path('ventas/', include('ventas.urls')),               # URLs para la aplicación de ventas
    path('almacen/', include('almacen.urls')),             # URLs para la aplicación de inventario
    path('pagos/', include('pagos.urls')),                 # URLs para la aplicación de pagos
    path('conteo-diario/', include('conteo_diario.urls')), # URLs para la aplicación de conteo diario
    path('sucursales/', include('sucursales.urls')),
]