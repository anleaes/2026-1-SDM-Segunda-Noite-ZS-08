from django.db import models
from pessoas.models import Pessoa
from planosmensalidade.models import PlanosMensalidade
from django.utils import timezone
import datetime

# Create your models here.
class Aluno(Pessoa):
    genero_opcoes = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'), 
    ]

    peso = models.FloatField('Peso', help_text='Preencha em kg (exemplo: 70.5)', blank=True, null=True)
    altura = models.FloatField('Altura',  help_text='Preencha em metros (exemplo: 1.70)', blank=True, null=True)
    genero = models.CharField('Gênero', max_length=1, choices=genero_opcoes)
    objetivo = models.TextField('Objetivo do aluno', blank=True, null=True)
    data_matricula = models.DateField('Data da matrícula', default=datetime.date.today)
    plano_mensalidade = models.ForeignKey(PlanosMensalidade, on_delete=models.SET_NULL, null=True, blank=True, related_name='alunos', verbose_name='Plano de Mensalidade')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural='Alunos'
        ordering=['id']
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.cpf}"