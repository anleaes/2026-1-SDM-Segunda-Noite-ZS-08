from django.db import models
from pessoas.models import Pessoa
import datetime

# Create your models here.
class Instrutor(Pessoa):
    especialidade_opcoes = [
        ('MUSC', 'Musculação'),
        ('FUNC', 'Treinamento Funcional'),
        ('PILA', 'Pilates'),
        ('CROS', 'Cross Training'),
        ('DANC', 'Dança / Ritmos'),
        ('LUTA', 'Artes Marciais'),
        ('NATA', 'Natação'),
        ('GERA', 'Ginástica Geral'),
    ]

    cref = models.CharField('CREF', max_length=12, unique=True, help_text='Exemplo: 000000-G/RS')
    especialidade = models.CharField('Especialidade', max_length=4, choices=especialidade_opcoes)
    salario = models.DecimalField('Salário', max_digits=10, decimal_places=2)
    data_admissao = models.DateField('Data de admissão', default=datetime.date.today)   