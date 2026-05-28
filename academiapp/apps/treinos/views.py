from django.shortcuts import render
from .models import Treino
from rest_framework import viewsets
from .serializers import TreinoSerializer

# Create your views here.
class TreinoViewSet(viewsets.ModelViewSet):
    pass