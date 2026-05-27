from django.db import models
from alunos.models import Aluno

# Create your models here.
class PlanoAlimentar(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='planos_alimentares', verbose_name='Aluno')
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)
    objetivo = models.CharField('Objetivo', max_length=150)
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim',blank=True, null=True)
    calorias_diarias = models.IntegerField('Calorias Diárias')
