from django.urls import path
from . import views

urlpatterns = [
    path('', views.sucursal_list, name='sucursal_list'),
    path('<int:pk>/', views.sucursal_detail, name='sucursal_detail'),
    path('nuevo/', views.sucursal_create, name='sucursal_create'),
    path('<int:pk>/editar/', views.sucursal_update, name='sucursal_update'),
    path('<int:pk>/eliminar/', views.sucursal_delete, name='sucursal_delete'),
]
