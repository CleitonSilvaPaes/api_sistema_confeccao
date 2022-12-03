from django.db import models
from usuario_sistema.models import UsuarioSistema
from cliente.models import Cliente
from status.models import Status
from django.core.validators import MaxValueValidator

class Pedido(models.Model):
    
    user_sistema = models.ForeignKey(UsuarioSistema, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nota_fiscal = models.IntegerField(null=False, blank=False, validators=[MaxValueValidator(9)], unique=True)
    data_entrega = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    item = models.CharField(max_length=50, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    status_pedido = models.ForeignKey(Status, on_delete=models.CASCADE)