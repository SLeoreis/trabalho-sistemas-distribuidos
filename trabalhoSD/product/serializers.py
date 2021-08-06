from rest_framework import serializers
from .models import *


class LivroArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroArtigo
        fields = '__all__'

class GeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geral
        fields = '__all__'

class ciclo_de_vidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciclo_de_vida
        fields = '__all__'

class meta_metadadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = meta_metadados
        fields = '__all__'        

class identificadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = identificador
        fields = '__all__'

class contribuinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = contribuinte
        fields = '__all__'

class metadados_tecnicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = metadados_tecnicos
        fields = '__all__'

class requisitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = requisitos
        fields = '__all__'        

class aspectos_EducacionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = aspectos_Educacionais
        fields = '__all__'

class direitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = direitos
        fields = '__all__'

class relacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = relacoes
        fields = '__all__'

class recursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = recurso
        fields = '__all__'        

class anotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = anotacao
        fields = '__all__'

class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao
        fields = '__all__'  