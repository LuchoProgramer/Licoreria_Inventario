from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                 # URL para el panel de administración de Django
    path('usuarios/', include('usuarios.urls')),     # Incluye las URLs de la aplicación 'usuarios'
    path('productos/', include('productos.urls')),   # Incluye las URLs de la aplicación 'productos'
    path('', include('usuarios.urls')),              # Redirige la raíz al archivo de URLs de usuarios
    path('ventas/', include('ventas.urls')),   # Incluye las URLs de la aplicación 'productos'
    path('sucursales/', include('sucursales.urls')),   # Incluye las URLs de la aplicación 'productos'
]
