from .models import Instrutor
from rest_framework import serializers

class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = '__all__'