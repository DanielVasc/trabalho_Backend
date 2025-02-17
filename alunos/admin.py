from django.contrib import admin
from .models import Clientes, Pedido, ItensPedido

admin.site.register(Clientes)
admin.site.register(Pedido)
admin.site.register(ItensPedido)