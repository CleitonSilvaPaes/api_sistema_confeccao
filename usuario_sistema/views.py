from django.shortcuts import render
from .serializers import UsuarioSistemaSerializer
from rest_framework.viewsets import generics
from rest_framework import viewsets
from .models import UsuarioSistema

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken



class UsuarioSistemaRegisterViewSet(viewsets.ModelViewSet):
    
    queryset = UsuarioSistema.objects.all()
    serializer_class = UsuarioSistemaSerializer
    http_method_names = ['post',]

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        print('-'*30)
        print(request)
        print('-'*30)
        
        return ObtainAuthToken().as_view()(request=request._request)