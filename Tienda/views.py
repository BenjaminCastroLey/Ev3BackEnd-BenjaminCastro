from django.shortcuts import render
from Tienda.models import categoria, Juego, Pedido

def index(request):
    productos = Juego.objects.all()
    data = {'productos': productos}
    return render(request, 'Index.html', data)
