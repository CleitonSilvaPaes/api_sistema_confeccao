from rest_framework import serializers
from usuario_sistema.models import UsuarioSistema
from dados_pagametos.models import DadosPagamentos
from .models import Fornecedor
from django.core.validators import MinLengthValidator, MaxLengthValidator


class FornecedorSerializer(serializers.ModelSerializer):
    banco = serializers.CharField(
        write_only=True,
        validators=[MaxLengthValidator(50)],
        required=False
    )
    conta = serializers.IntegerField(
        write_only=True,
        validators=[MaxLengthValidator(8)],
        required=False
    )
    agencia = serializers.IntegerField(
        write_only=True,
        validators=[MaxLengthValidator(4)],
        required=False
    )
    pix = serializers.CharField(
        write_only=True,
        validators=[MaxLengthValidator(50), MinLengthValidator(6)],
        required=True
    )
    
    class Meta:
       model = Fornecedor
       exclude = ['user_sistema', 'dados_pagamentos']
    
    def validate(self, attrs):
        msg = {}
        banco = attrs.get('banco', None)
        conta = attrs.get('conta', None)
        agencia = attrs.get('agencia', None)
        pix = attrs.get('pix')
        user = self.context['request'].user
        user_sistema = UsuarioSistema(user=user)
        dados_pagamentos = DadosPagamentos.objects.filter(pix=pix)
               
        if dados_pagamentos == 0:
            dados_pagamentos = DadosPagamentos.objects.create(banco=banco, conta=conta, agencia=agencia, pix=pix)
        else:
            msg['pix'] = 'Infelizmente, pix não aceito, digite outro'
            raise serializers.ValidationError(msg)
        attrs['user_sistema'] = user_sistema
        attrs['dados_pagamentos'] = dados_pagamentos
        
        return attrs
    
    def create(self, validated_data):
        
        nome = validated_data.get('nome')
        telefone = validated_data.get('telefone')
        descricao = validated_data.get('descricao')
        user_sistema = validated_data.get('user_sistema')
        dados_pagamentos = validated_data.get('dados_pagamentos')
        
        fornecedor = Fornecedor.objects.create(user_sistema=user_sistema, nome=nome, telefone=telefone, descricao=descricao, dados_pagamentos=dados_pagamentos)
        
        return fornecedor
        