from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from product.views import *


urlpatterns = [
    path('cadastro/', views.CadastroList.as_view()),
    path('cadastro/<int:pk>/', views.CadastroDetail.as_view()),
]