from django.db import models
from django.contrib.auth.models import User
from dados_pagametos.models import DadosPagamentos
from django.core.validators import MinLengthValidator



class UsuarioSistema(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    endereco = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    dados_pagamentos = models.ForeignKey(DadosPagamentos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username