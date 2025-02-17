from rest_framework.serializers import ModelSerializer
from .models import Clientes, Pedido, ItensPedido

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItensPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'