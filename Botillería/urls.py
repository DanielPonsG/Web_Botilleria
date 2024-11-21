from django.contrib import admin
from django.urls import path
from BotilleríaApp.views import Index 
from BotilleríaApp.views import Carta
from BotilleríaApp.views import Ingresar
from BotilleríaApp.views import Productos
from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='Inicio'),
    path('Carta/', Carta, name='Carta'),
    path('Ingresar/', Ingresar, name='Ingresar'),
    path('Productos/', Productos, name='Productos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
