# usuarios/views.py
from django.http import HttpResponse
from django.shortcuts import render

def login_view(request):
    return HttpResponse("Página de inicio de sesión")

def logout_view(request):
    return HttpResponse("Página de cierre de sesión")

def perfil_view(request):
    return HttpResponse("Página de perfil del usuario")

def registro_view(request):
    return HttpResponse("Página de registro de nuevos usuarios")
