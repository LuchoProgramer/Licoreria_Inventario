# ventas/views.py
from django.http import HttpResponse
from django.shortcuts import render

def ventas_list(request):
    return HttpResponse("Listado de ventas")

def venta_detail(request, id):
    return HttpResponse(f"Detalle de la venta con ID {id}")

def venta_create(request):
    return HttpResponse("Crear una nueva venta")

def cierre_caja(request):
    return HttpResponse("Cierre de caja diario")
