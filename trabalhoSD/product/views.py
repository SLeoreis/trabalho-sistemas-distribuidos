from .models import *
from .serializers import *
from rest_framework import generics, permissions, serializers, viewsets


class CadastroViewSet (viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer