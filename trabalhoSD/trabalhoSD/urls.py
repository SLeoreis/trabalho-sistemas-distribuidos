
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls, routers

from rest_framework.urlpatterns import format_suffix_patterns
from product import views
from product.views import ciclo_de_vidaList

urlpatterns = [
    path('ciclo_de_vida/', ciclo_de_vidaList.as_view()),
    path('ciclo_de_vida/<int:pk>/', views.ciclo_de_vidaDetail.as_view()),
]

