import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class categoria(models.Model):
    Categoria_id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, unique=True)
    Descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre

class Juego(models.Model):
    Juego_id = models.AutoField(primary_key=True)
    Categoria_id = models.ForeignKey(categoria, on_delete=models.CASCADE)
    ImagenCaja = models.ImageField(upload_to='ImagenCaja/', null=True, blank=True)
    Nombre = models.CharField(max_length=50)
    Valor = models.IntegerField()
    EdadRequerida = models.IntegerField()
    CantidadJugadores = models.IntegerField()
    Stock = models.IntegerField()
    EstadoVenta = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre


def generar_codigo_identificacion():
    return uuid.uuid4().hex[:10].upper()


class Pedido(models.Model):
    Pedido_id = models.AutoField(primary_key=True)
    Juego_id = models.ForeignKey(Juego, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Correo = models.EmailField(blank=True)
    CantidadPedido = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    DateTime = models.DateTimeField(auto_now_add=True)
    CodigoIdentificacion = models.CharField(
        max_length=10,
        unique=True,
        default=generar_codigo_identificacion,
        editable=False
    )

    def __str__(self):
        return self.Nombre