from .models import Treino
from rest_framework import serializers

class TreinoSerializer(serializers.ModelSerializer):

   exercicios = serializers.SerializerMethodField()

   class Meta:
      model = Treino
      fields = '__all__'

   def get_exercicios(self, obj):
      return list(obj.itens.values_list('exercicio_id', flat=True))