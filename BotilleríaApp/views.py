from django.shortcuts import render
from BotilleríaApp.models import Botellas
# Create your views here.
def Index(request):
    return render(request,'index.html')


def Productos(request):
    producto = Botellas.objects.all()
    return render(request,'product.html',{'producto':producto})


def Ingresar(request):
    return render(request,'index.html')


def Carta(request):
    return render(request,'cart.html')