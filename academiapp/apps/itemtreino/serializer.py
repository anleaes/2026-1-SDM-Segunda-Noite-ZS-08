from .models import ItemTreino
from rest_framework import serializers
    
class ItemTreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTreino
        fields = '__all__'