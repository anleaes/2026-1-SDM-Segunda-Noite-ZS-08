from django.shortcuts import render
from .models import ItemTreino
from rest_framework import viewsets
from .serializer import  ItemtreinoSerializer

# Create your views here.
class ItemTreinoViewSet(viewsets.ModelViewSet):
    queryset = ItemTreino.objects.all()
    serializer_class = ItemtreinoSerializer 
