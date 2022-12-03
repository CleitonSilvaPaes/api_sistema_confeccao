from .models import Cliente
from usuario_sistema.models import UsuarioSistema
from .serializers import ClienteSerialiazer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        usuario_sistema = UsuarioSistema.objects.get(user=user)
        return Cliente.objects.filter(usuario_sistema=usuario_sistema)
    
    serializer_class = ClienteSerialiazer
