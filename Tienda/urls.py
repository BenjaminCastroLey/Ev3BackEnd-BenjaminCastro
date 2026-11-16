from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('compra-exitosa/<int:pedido_id>/', views.compra_exitosa, name='compra_exitosa'),
]
