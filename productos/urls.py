from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_list, name='productos_list'),                    # Listado de productos
    path('<int:id>/', views.producto_detail, name='producto_detail'),         # Detalle de un producto
    path('crear/', views.producto_create, name='producto_create'),            # Crear un nuevo producto
    path('editar/<int:id>/', views.producto_update, name='producto_update'),  # Editar un producto existente
    path('eliminar/<int:id>/', views.producto_delete, name='producto_delete'),# Eliminar un producto
]
