
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls, routers
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from product import views
from product.views import LivroArtigoList, LivroArtigoDetail

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('LivroArtigo/', views.LivroArtigoList.as_view()),
    path('LivroArtigo/<int:pk>/', views.LivroArtigoDetail.as_view()),
]
