from django.shortcuts import render
from .models import Instrutor
from rest_framework import viewsets
from .serializer import InstrutorSerializer

# Create your views here.
class InstrutorViewSet (viewsets.ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer