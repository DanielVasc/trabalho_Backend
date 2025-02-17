from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    numero_pedido = models.IntegerField()
    data_compra = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
        
    def __str__(self):
            return f'Pedido {self.numero_pedido} - {self.cliente.nome}'
        
class ItensPedido(models.Model):
    id = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.id_pedido.numero_pedido} - {self.produto}'