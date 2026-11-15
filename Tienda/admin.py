from django.contrib import admin
from Tienda.models import categoria, Juego, Pedido

# Register your models here.

admin.site.register(categoria)
admin.site.register(Juego)
admin.site.register(Pedido)