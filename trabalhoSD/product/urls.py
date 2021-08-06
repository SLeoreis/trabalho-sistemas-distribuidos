from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
   path('api', include('product.urls')),
    path('admin/', admin.site.urls),
]