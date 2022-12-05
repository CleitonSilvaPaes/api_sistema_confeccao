from rest_framework import viewsets
from .serializers import Fornecedor, FornecedorSerializer
from rest_framework.permissions import IsAuthenticated
from usuario_sistema.models import UsuarioSistema


class FornecedorViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]   
    serializer_class = FornecedorSerializer
    def get_queryset(self):
        user = self.request.user
        user_sistema = UsuarioSistema.objects.get(user=user)
        return Fornecedor.objects.filter(user_sistema=user_sistema)
