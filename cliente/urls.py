from django.urls import path, include
from rest_framework import routers
from .views import ClienteViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('', ClienteViewSet, basename='cliente')

cliente_urls = [
    path('', include(router.urls))
]