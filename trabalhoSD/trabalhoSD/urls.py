
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls, routers
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from product import views
from product.views import * 


urlpatterns = [
    path('api/', include('product.urls')),
    path('admin/', admin.site.urls),
]