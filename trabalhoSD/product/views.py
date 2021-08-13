from .models import *
from .serializers import *
from rest_framework import generics, permissions, serializers, viewsets

class CadastroList(generics.ListCreateAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer

class CadastroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    