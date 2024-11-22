from django.contrib import admin
from BotilleríaApp.models import Botellas
# Register your models here.

class BotellasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','precio','descripcion']

admin.site.register(Botellas, BotellasAdmin)
