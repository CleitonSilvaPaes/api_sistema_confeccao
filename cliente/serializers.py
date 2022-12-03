from rest_framework import serializers
from .models import Cliente
from usuario_sistema.models import UsuarioSistema

class ClienteSerialiazer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cnpj']
        
    def validate(self, attrs):
        user = self.context['request'].user
        usuario_sistema = UsuarioSistema.objects.get(user=user)
        attrs['usuario_sistema'] = usuario_sistema
        return super().validate(attrs)