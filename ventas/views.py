# ventas/views.py
from django.http import HttpResponse

def sales_summary(request):
    return HttpResponse("Resumen de ventas en construcción")
