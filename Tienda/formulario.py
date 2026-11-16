from django import forms

class FormVenta(forms.Form):

    Juego_id = forms.CharField()
    Nombre = forms.CharField()
    Correo = forms.CharField()
    CantidadPedido = forms.IntegerField()