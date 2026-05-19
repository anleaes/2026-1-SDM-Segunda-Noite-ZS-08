from django.shortcuts import render
from .models import Alunos
from rest_framework import viewsets
from .serializer import AlunoSerializer

# Create your views here.
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer