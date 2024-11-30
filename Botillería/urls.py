from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from BotilleríaApp.views import Index, Ingresar, Productos, registro, ver_carrito
from BotilleríaApp.views import login_view, logout_view, agregar_al_carrito, ver_carrito


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='Inicio'),
    path('registro/', registro, name='registro'),
    path('ingresar/', Ingresar, name='ingresar'),
    path('productos/', Productos, name='productos'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
