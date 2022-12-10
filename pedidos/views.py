from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import response

from usuario_sistema.models import UsuarioSistema

from .models import Pedidos
from .serializers import PedidosSerializer


class PedidosViewSet(viewsets.ModelViewSet):

    # queryset = Pedidos.objects.all()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        usuario_sistema = UsuarioSistema.objects.get(user=user)
        return Pedidos.objects.filter(usuario_sistema=usuario_sistema)

    serializer_class = PedidosSerializer
