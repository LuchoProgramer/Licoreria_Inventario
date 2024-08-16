from django.shortcuts import render, get_object_or_404, redirect
from .models import Sucursal
from .forms import SucursalForm

def sucursal_list(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales/sucursal_list.html', {'sucursales': sucursales})

def sucursal_create(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucursal_list')
    else:
        form = SucursalForm()
    return render(request, 'sucursales/sucursal_form.html', {'form': form})

def sucursal_update(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('sucursal_list')
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'sucursales/sucursal_form.html', {'form': form})

def sucursal_detail(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    return render(request, 'sucursales/sucursal_detail.html', {'sucursal': sucursal})

def sucursal_delete(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('sucursal_list')
    return render(request, 'sucursales/sucursal_confirm_delete.html', {'sucursal': sucursal})
