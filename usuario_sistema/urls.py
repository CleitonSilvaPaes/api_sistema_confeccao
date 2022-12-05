from django.urls import path, include
from rest_framework import routers
from .views import UsuarioSistemaRegisterViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register('login', LoginViewSet, basename='login')
router.register('signup', UsuarioSistemaRegisterViewSet, basename='signup')

usuario_sistema_urls = [
    path('', include(router.urls))
]