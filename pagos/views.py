# pagos/views.py
from django.http import HttpResponse
from django.shortcuts import render

def pagos_list(request):
    return HttpResponse("Listado de pagos")

def pago_detail(request, id):
    return HttpResponse(f"Detalle del pago con ID {id}")

def registrar_pago(request):
    return HttpResponse("Registrar un nuevo pago")
