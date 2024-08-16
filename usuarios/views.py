# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Vista para la página de registro
# Verificar que el usuario es administrador
def admin_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)

@admin_required
@login_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al administrador a la página de usuarios o alguna página de éxito
            return redirect('admin_dashboard')  # Asegúrate de tener una vista 'admin_dashboard'
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {
        'form': form
    })
    
# Vista para la página de inicio
@login_required
def home(request):
    user = request.user
    context = {
        'is_admin': user.is_superuser,
        # Puedes agregar más contexto según sea necesario
    }
    return render(request, 'home.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def daily_count(request):
    return render(request, 'daily_count.html')

@login_required
def product_sales(request):
    return render(request, 'product_sales.html')

@login_required
def payments(request):
    return render(request, 'payments.html')

@login_required
def invoicing(request):
    return render(request, 'invoicing.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')