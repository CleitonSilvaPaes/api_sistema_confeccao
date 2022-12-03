from django.urls import path, include
from rest_framework import routers
from .views import FornecedorViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('', FornecedorViewSet, basename='fornecedor')

fornecedor_urls = [
    path('', include(router.urls))
]