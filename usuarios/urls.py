from django.contrib import admin
# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('daily_count/', views.daily_count, name='daily_count'),
    path('product_sales/', views.product_sales, name='product_sales'),
    path('payments/', views.payments, name='payments'),
    path('invoicing/', views.invoicing, name='invoicing'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # Agrega otras rutas aquí
]