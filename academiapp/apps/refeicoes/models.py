from django.db import models
from apps.alimentos.models import Alimento
from apps.planosalimentares.models import PlanoAlimentar

class Refeicao(models.Model):
    nome = models.CharField(max_length=150)
    horario = models.DateTimeField()
    descricao = models.TextField()
    plano_alimentar = models.ForeignKey(PlanoAlimentar, on_delete=models.CASCADE)
    alimentos = models.ManyToManyField(Alimento)
    
    
class Meta:
        db_table = 'refeicoes'
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'

def __str__(self):
        return self.nome