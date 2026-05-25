from .models import Itemtreino
from rest_framework import serializers
    
class ItemtreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemtreino
        fields = '__all__'