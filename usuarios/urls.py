from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),          # Página de inicio de sesión
    path('logout/', views.logout_view, name='logout'),       # Página de cierre de sesión
    path('perfil/', views.perfil_view, name='perfil'),       # Página de perfil del usuario
    path('registro/', views.registro_view, name='registro'), # Página de registro de nuevos usuarios
]
