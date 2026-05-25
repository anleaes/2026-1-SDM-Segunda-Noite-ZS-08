from django.shortcuts import render
from .models import Treino
from rest_framework import viewsets
from .serializer import TreinoSerializer

# Create your views here.
class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer  
