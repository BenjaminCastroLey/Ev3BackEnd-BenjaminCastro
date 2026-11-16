from django.shortcuts import render, redirect
from Tienda.models import categoria, Juego, Pedido
from Tienda.formulario import FormVenta


def index(request):
    productos = Juego.objects.all()
    data = {'productos': productos}
    return render(request, 'Index.html', data)


def comprar(request, id):
    producto = Juego.objects.get(Juego_id=id)
    form = FormVenta(initial={'Juego_id': producto.Juego_id})

    if request.method == 'POST':
        form = FormVenta(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['CantidadPedido']

            if cantidad > producto.Stock:
                form.add_error('CantidadPedido', 'La cantidad solicitada supera el stock disponible.')
            else:
                producto.Stock = producto.Stock - cantidad
                producto.EstadoVenta = producto.Stock > 0
                producto.save()

                pedido = Pedido(
                    Juego_id=producto,
                    Nombre=form.cleaned_data['Nombre'],
                    Correo=form.cleaned_data['Correo'],
                    CantidadPedido=cantidad
                )
                pedido.save()
                return redirect('compra_exitosa', pedido_id=pedido.Pedido_id)

    data = {
        'juego': producto,
        'form': form
    }
    return render(request, 'comprar.html', data)


def compra_exitosa(request, pedido_id):
    pedido = Pedido.objects.get(Pedido_id=pedido_id)
    data = {
        'pedido': pedido,
        'juego': pedido.Juego_id,
    }
    return render(request, 'compra_exitosa.html', data)
