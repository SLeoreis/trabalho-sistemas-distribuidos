
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls, routers
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns 
from product.views import CadastroViewSet

api_router = routers.DefaultRouter()
api_router.register(r"cadastro", CadastroViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]