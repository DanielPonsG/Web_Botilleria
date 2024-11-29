from django.contrib import admin
from BotilleríaApp.models import Botellas, Carrito, PerfilUsuario, ItemCarrito, User

# Register your models here.

class BotellasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','precio','descripcion']

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'producto', 'cantidad']  # Campos a mostrar


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'direccion', 'telefono']  # Campos a mostrar

class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 1

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    inlines = [ItemCarritoInline]



admin.site.register(Botellas, BotellasAdmin)
admin.site.register(PerfilUsuario, PerfilAdmin)
admin.site.register(Carrito, CarritoAdmin)



