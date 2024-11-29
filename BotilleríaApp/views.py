from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from BotilleríaApp.models import Botellas, Carrito, User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Carrito, ItemCarrito
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

# Registro de Usuarios
def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return redirect('registro')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Te has registrado correctamente.')
        login(request, user)  # Iniciar sesión automáticamente después del registro
        return render(request, 'product.html')

    # Si no es una solicitud POST, renderiza el formulario de registro
    return render(request, 'register.html')

# Inicio de Sesion y Vista de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista de Logout 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Inicio')

# Vista de Carrito
def ver_carrito(request):
    # Obtener el carrito del usuario actual
    carrito = Carrito.objects.filter(usuario=request.user).first()

    if carrito:
        items = ItemCarrito.objects.filter(carrito=carrito)  # Obtener todos los items en el carrito
        total = sum([item.botella.precio * item.cantidad for item in items])  # Sumar el precio total
    else:
        items = []
        total = 0
    
    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })

def Index(request):
    return render(request,'index.html')

def Productos(request):
    producto = Botellas.objects.all()
    return render(request,'product.html',{'producto':producto})


def Ingresar(request):
    return render(request,'index.html')

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Botellas, id=producto_id)

    # Obtener el carrito del usuario actual
    carrito, created = ItemCarrito.objects.get_or_create(usuario=request.user)

    # Crear un item en el carrito
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, botella=producto)
    if not created:
        item.cantidad += 1
        item.save()

    messages.success(request, f"{producto.nombre} se ha agregado al carrito.")
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    # Obtener el carrito del usuario actual
    carrito = Carrito.objects.filter(usuario=request.user).first()

    items = ItemCarrito.objects.filter(carrito=carrito) if carrito else []
    total = sum([item.botella.precio * item.cantidad for item in items])
    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })