from .models import Alimento
from rest_framework import  serializers

class AlimentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'