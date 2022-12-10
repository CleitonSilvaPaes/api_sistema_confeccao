from rest_framework import serializers
from usuario_sistema.models import UsuarioSistema
from cliente.models import Cliente
from status.models import Status
from .models import Pedidos


class PedidosSerializer(serializers.ModelSerializer):
    STATUS = (
        ('N', 'Novo'),
        ('I', 'Iniciado'),
        ('F', 'Finalizado'),
        ('E', 'Entrege')
    )
    status = serializers.ChoiceField(
        choices=STATUS
    )

    class Meta:
        model = Pedidos
        fields = '__all__'
        # exclude = ['usuario_sistema',]

    # def to_representation(self, instance):
    #    representation = super().to_representation(instance)

    def validate(self, attrs):
        # user = self.context['request'].user
        # usuario_sistema = UsuarioSistema.objects.get(user=user)
        # attrs['usuario_sistema'] = usuario_sistema
        valor = attrs.get('valor')
        if valor <= 0:
            raise serializers.ValidationError(
                {'valor': 'Tem que ser valor positivo'})
        return super().validate(attrs)

    def create(self, validated_data):
        print(validated_data)
        item = validated_data['item']
        nota_fiscal = validated_data['nota_fiscal']
        valor = validated_data['valor']
        usuario_sistema = validated_data['usuario_sistema']
        cliente = validated_data['cliente']
        data_entrega = validated_data['data_entrega']
        # raise serializers.ValidationError()
        status = Status.objects.create(status=validated_data['status'])
        pedido = Pedidos.objects.create(
            usuario_sistema=usuario_sistema, item=item, nota_fiscal=nota_fiscal, valor=valor, data_entrega=data_entrega,
            cliente=cliente, status=status)
        return pedido
    
    def update(self, instance, validated_data):
        status = Status.objects.get(pk=instance.status.id)
        status.status = validated_data.get('status', 'N')
        status.save()
        instance.status = status
        instance.item = validated_data.get('item', instance.item)
        instance.nota_fiscal = validated_data.get('nota_fiscal', instance.nota_fiscal)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.data_entrega = validated_data.get('data_entrega', instance.data_entrega)
        instance.usuario_sistema = validated_data.get('usuario_sistema', instance.usuario_sistema)
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.save()
        return instance