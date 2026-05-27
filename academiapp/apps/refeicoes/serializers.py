from .models import Refeicao
from rest_framework import serializers

class RefeicaoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Refeicao
        fields = '__all__'