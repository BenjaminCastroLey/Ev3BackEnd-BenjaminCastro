from django import forms


class FormVenta(forms.Form):
    Juego_id = forms.CharField(widget=forms.HiddenInput())
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    CantidadPedido = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}))