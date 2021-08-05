from .models import ciclo_de_vida
from .serializers import ciclo_de_vidaSerializer
from rest_framework import serializers, viewsets, generics

class ciclo_de_vidaList(generics.ListCreateAPIView):
    queryset = ciclo_de_vida.objects.all()
    serializer_class = ciclo_de_vidaSerializer

class ciclo_de_vidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ciclo_de_vida.objects.all()
    serializer_class = ciclo_de_vidaSerializer

