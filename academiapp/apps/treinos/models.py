from django.db import models
from alunos.models import Aluno
from instrutores.models import Instrutor



# Create your models here.
class Treino(models.Model):

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='treinos')
    instrutor = models.ForeignKey(Instrutor, on_delete=models.SET_NULL, null=True, related_name='treinos_criados')
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    duracao_minutos = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.aluno.nome}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    