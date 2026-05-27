from .models import Exercicio
from rest_framework import serializers

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'
        