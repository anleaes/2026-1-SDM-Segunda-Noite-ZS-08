from rest_framework import serializers
from .models import PlanoAlimentar

class PlanoAlimentarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoAlimentar
        fields = '__all__'