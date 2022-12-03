from rest_framework import serializers
from .models import UsuarioSistema
from dados_pagametos.models import DadosPagamentos
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class UsuarioSistemaSerializer(serializers.ModelSerializer):

    usuario = serializers.CharField(
        write_only=True,
        required=True,
    )
    senha = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[MaxLengthValidator(50), MinLengthValidator(8)]
    )
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
        model = UsuarioSistema
        fields = ['usuario', 'senha', 'cpf', 'endereco',
                  'banco', 'conta', 'agencia', 'pix',]

    def validate(self, attrs):
        msg = {}
        nome = attrs.get('usuario')
        senha = attrs.get('senha')
        cpf = attrs.get('cpf')
        endereco = attrs.get('endereco')
        banco = attrs.get('banco', None)
        conta = attrs.get('conta', None)
        agencia = attrs.get('agencia', None)
        pix = attrs.get('pix')

        user = User.objects.filter(username=nome)
        dados_pagamentos = DadosPagamentos.objects.filter(pix=pix)
        if len(user) == 0:
            user = User.objects.create_user(username=nome, password=senha)
            attrs['user'] = user
        else:
            msg['user'] = 'Infelizmente, esse usuario já existe, digite outro'
            raise serializers.ValidationError(msg)
        if len(dados_pagamentos) == 0:
            dados_pagamentos = DadosPagamentos.objects.create(
                banco=banco, conta=conta, agencia=agencia, pix=pix)
            attrs['dados_pagamentos'] = dados_pagamentos
        else:
            msg['pix'] = 'Infelizmente, esse pix não é aceito digite outro'
            raise serializers.ValidationError(msg)

        if cpf.isalpha():
            msg['cpf'] = 'digite somente numero'
            raise serializers.ValidationError(msg)
        return attrs

    def create(self, validated_data):

        cpf = validated_data.get('cpf')
        endereco = validated_data.get('endereco')
        user = validated_data.get('user')
        dados_pagamentos = validated_data.get('dados_pagamentos')

        usuario_sistema = UsuarioSistema.objects.create(
            user=user, endereco=endereco, cpf=cpf, dados_pagamentos=dados_pagamentos)

        return usuario_sistema
