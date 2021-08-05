from rest_framework import serializers
from .models import ciclo_de_vida


class ciclo_de_vidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciclo_de_vida
        fields =('id','versao','status','entidade','datas',
                )