from .models import Anamneses
from rest_framework import serializers

class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamneses
        fields = '__all__'