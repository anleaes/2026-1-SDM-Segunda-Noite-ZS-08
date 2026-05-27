from django.db import models
from apps.alimentos.models import Alimento
from apps.planosalimentares.models import PlanoAlimentar

class Refeicao(models.Model):
    nome = models.CharField(max_length=150)
    horario = models.DateTimeField()
    descricao = models.TextField()
    plano_alimentar = models.ForeignKey(PlanoAlimentar, on_delete=models.CASCADE)
    alimentos = models.ManyToManyField(Alimento)