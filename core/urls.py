"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuario_sistema.urls import usuario_sistema_urls
from cliente.urls import cliente_urls
from fornecedor.urls import fornecedor_urls
from pedidos.urls import pedidos_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(usuario_sistema_urls)),
    path('cliente/', include(cliente_urls)),
    path('fornecedor/', include(fornecedor_urls)),
    path('pedido/', include(pedidos_urls)),
]
