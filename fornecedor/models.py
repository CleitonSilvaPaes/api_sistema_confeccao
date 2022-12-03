from django.db import models
from usuario_sistema.models import UsuarioSistema
from dados_pagametos.models import DadosPagamentos
from django.core.validators import MinLengthValidator


class Fornecedor(models.Model):
    
    user_sistema = models.ForeignKey(UsuarioSistema, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=False, null=False)
    telefone = models.CharField(max_length=9, validators=[MinLengthValidator(9)], blank=False, null=False)
    descricao = models.CharField(max_length=250, blank=False, null=False)
    dados_pagamentos = models.ForeignKey(DadosPagamentos, on_delete=models.CASCADE, null=False, blank=False)