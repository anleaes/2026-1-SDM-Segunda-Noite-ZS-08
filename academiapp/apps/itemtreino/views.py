from django.shortcuts import render
from .models import ItemTreino
from rest_framework import viewsets
from .serializer import  ItemTreinoSerializer

# Create your views here.
class ItemTreinoViewSet(viewsets.ModelViewSet):
    pass