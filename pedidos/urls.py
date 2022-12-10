from django.urls import path, include
from rest_framework import routers
from .views import PedidosViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('', PedidosViewSet, basename='pedido')

pedidos_urls = [
    path('', include(router.urls))
]