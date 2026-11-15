from django.contrib import admin
from django.utils.html import format_html
from Tienda.models import categoria, Juego, Pedido

# Register your models here.

class categoriaForm(admin.ModelAdmin):
    list_display = ['Nombre']

class JuegoForm(admin.ModelAdmin):
    list_display = ['ImagenCaja', 'Nombre', 'Valor', 'Stock', 'EstadoVenta']

    @admin.display(description='Imagen')
    def imagen_previa(self, obj):
        if obj.ImagenCaja and obj.ImagenCaja.url:
            return format_html(
                '<img src="{}" width="60" heigth="60" style="object-fit:cover; border-radius:6px" />',
                obj.ImagenCaja.url
            )
        return "Sin imagen"


class PedidoForm(admin.ModelAdmin):
    list_display = ['Nombre', 'Correo', 'CodigoIdentificacion']

admin.site.register(categoria, categoriaForm)
admin.site.register(Juego, JuegoForm)
admin.site.register(Pedido, PedidoForm)