from django.shortcuts import render
from Tienda.models import categoria, Juego, Pedido
from Tienda.formulario import FormVenta

def index(request):
    productos = Juego.objects.all()
    data = {'productos': productos}
    return render(request, 'Index.html', data)

def comprar(request, id):

    producto = Juego.objects.get(Juego_id=id)
    form = FormVenta(initial={'Juego_id': producto.Juego_id})
    data = {
        'juego': producto,
        'form': form
    }
    return render(request, 'comprar.html', data)
