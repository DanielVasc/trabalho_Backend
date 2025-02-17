from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Clientes, Pedido, ItensPedido
from .serializers import ClientesSerializer, PedidoSerializer, ItensPedidoSerializer

class ClientesViewSet(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItensPedidoViewSet(ModelViewSet):
    queryset = ItensPedido.objects.all()
    serializer_class = ItensPedidoSerializer