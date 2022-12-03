from django.db import models
from usuario_sistema.models import UsuarioSistema
from django.core.validators import MinLengthValidator


class Cliente(models.Model):
    
    usuario_sistema = models.ForeignKey(UsuarioSistema, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=15, validators=[MinLengthValidator(15)], blank=True)
    
    def __str__(self):
        return self.nome