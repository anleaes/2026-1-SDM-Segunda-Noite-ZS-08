from .models import PlanoAlimentar
from rest_framework import serializers

class PlanoAlimentarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoAlimentar
        fields = '__all__'