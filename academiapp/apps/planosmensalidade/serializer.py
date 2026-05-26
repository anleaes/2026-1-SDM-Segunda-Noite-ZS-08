from .models import PlanosMensalidade
from rest_framework import serializers

class PlanosMensalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanosMensalidade
        fields = '__all__'