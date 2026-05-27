from django.shortcuts import render
from .models import Refeicao
from rest_framework import viewsets
from .serializers import RefeicaoSerializer

# Create your views here.
class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer