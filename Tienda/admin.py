from django.contrib import admin
from django.utils.html import format_html
from Tienda.models import categoria, Juego, Pedido
from django.contrib.humanize.templatetags.humanize import intcomma

# Register your models here.

class categoriaForm(admin.ModelAdmin):
    list_display = ['Nombre']

class JuegoForm(admin.ModelAdmin):
    list_display = ['ImagenCaja', 'Nombre', 'precio_clp', 'Stock', 'EstadoVenta']

    @admin.display(description='Imagen')
    def imagen_previa(self, obj):
        if obj.ImagenCaja and obj.ImagenCaja.url:
            return format_html(
                '<img src="{}" width="60" heigth="60" style="object-fit:cover; border-radius:6px" />',
                obj.ImagenCaja.url
            )
        return "Sin imagen"

    @admin.display(description='Precio')
    def precio_clp(self, obj):
        return f"$ {intcomma(obj.Valor)}"   


class PedidoForm(admin.ModelAdmin):
    list_display = ['Nombre', 'Correo', 'CodigoIdentificacion']

admin.site.register(categoria, categoriaForm)
admin.site.register(Juego, JuegoForm)
admin.site.register(Pedido, PedidoForm)