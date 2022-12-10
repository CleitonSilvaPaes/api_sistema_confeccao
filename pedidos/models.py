from django.db import models
from usuario_sistema.models import UsuarioSistema
from cliente.models import Cliente
from status.models import Status

class Pedidos(models.Model):
    usuario_sistema = models.ForeignKey(
        UsuarioSistema, on_delete=models.CASCADE)
    item = models.CharField(max_length=250)
    nota_fiscal = models.IntegerField()
    valor = models.FloatField()
    data_entrega = models.DateField(auto_now=False, auto_now_add=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
