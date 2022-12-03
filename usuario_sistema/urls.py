from django.urls import path, include
from rest_framework import routers
from .views import UsuarioSistemaRegisterAPIView, LoginViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('login', LoginViewSet, basename='login')

usuario_sistema_urls = [
    path('signup', UsuarioSistemaRegisterAPIView.as_view()),
    path('', include(router.urls))
]