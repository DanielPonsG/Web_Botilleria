from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')


def Productos(request):
    return render(request,'product.html')


def Ingresar(request):
    return render(request,'index.html')


def Carta(request):
    return render(request,'cart.html')