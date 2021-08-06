from .models import *
from .serializers import *
from rest_framework import serializers, viewsets, generics

class LivroArtigoList(generics.ListCreateAPIView):
    queryset = LivroArtigo.objects.all()
    serializer_class = LivroArtigoSerializer

class LivroArtigoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivroArtigo.objects.all()
    serializer_class = LivroArtigoSerializer


class GeralList(generics.ListCreateAPIView):
    queryset = Geral.objects.all()
    serializer_class = GeralSerializer

class GeralDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geral.objects.all()
    serializer_class = GeralSerializer


class ciclo_de_vidaList(generics.ListCreateAPIView):
    queryset = ciclo_de_vida.objects.all()
    serializer_class = ciclo_de_vidaSerializer

class ciclo_de_vidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ciclo_de_vida.objects.all()
    serializer_class = ciclo_de_vidaSerializer


class meta_metadadosList(generics.ListCreateAPIView):
    queryset = meta_metadados.objects.all()
    serializer_class = meta_metadadosSerializer

class meta_metadadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = meta_metadados.objects.all()
    serializer_class = meta_metadadosSerializer


class identificadorList(generics.ListCreateAPIView):
    queryset = identificador.objects.all()
    serializer_class = identificadorSerializer

class identificadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = identificador.objects.all()
    serializer_class = identificadorSerializer


class contribuinteList(generics.ListCreateAPIView):
    queryset = contribuinte.objects.all()
    serializer_class = contribuinteSerializer

class contribuinteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = contribuinte.objects.all()
    serializer_class = contribuinteSerializer


class metadados_tecnicosList(generics.ListCreateAPIView):
    queryset = metadados_tecnicos.objects.all()
    serializer_class = metadados_tecnicosSerializer

class metadados_tecnicosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = metadados_tecnicos.objects.all()
    serializer_class = metadados_tecnicosSerializer


class requisitosList(generics.ListCreateAPIView):
    queryset = requisitos.objects.all()
    serializer_class = requisitosSerializer

class requisitosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = requisitos.objects.all()
    serializer_class = requisitosSerializer


class aspectos_EducacionaisList(generics.ListCreateAPIView):
    queryset = aspectos_Educacionais.objects.all()
    serializer_class = aspectos_EducacionaisSerializer

class aspectos_EducacionaisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = aspectos_Educacionais.objects.all()
    serializer_class = aspectos_EducacionaisSerializer


class direitosList(generics.ListCreateAPIView):
    queryset = direitos.objects.all()
    serializer_class = direitosSerializer

class direitosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = direitos.objects.all()
    serializer_class = direitosSerializer


class relacoesList(generics.ListCreateAPIView):
    queryset = relacoes.objects.all()
    serializer_class = relacoesSerializer

class relacoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = relacoes.objects.all()
    serializer_class = relacoesSerializer


class recursoList(generics.ListCreateAPIView):
    queryset = recurso.objects.all()
    serializer_class = recursoSerializer

class recursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = recurso.objects.all()
    serializer_class = recursoSerializer


class anotacaoList(generics.ListCreateAPIView):
    queryset = anotacao.objects.all()
    serializer_class = anotacaoSerializer

class anotacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = anotacao.objects.all()
    serializer_class = anotacaoSerializer


class ClassificacaoList(generics.ListCreateAPIView):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer

class ClassificacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer