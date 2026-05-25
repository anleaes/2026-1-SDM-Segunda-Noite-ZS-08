from django.db import models

# Create your models here.
class Exercicio(models.Model):
    DIFICULDADE_CHOICES = [
        ('F', 'Fácil'),
        ('M', 'Médio'),
        ('D', 'Díficil'),
    ]

    nome = models.CharField(
        max_length=100, 
        verbose_name="Nome do Exercício"
    )
    descricao = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Descrição"
    )
    instrucoes = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Instruções de Execução"
    )
    dificuldade = models.CharField(
        max_length=1, 
        choices=DIFICULDADE_CHOICES, 
        default='F', 
        verbose_name="Grau de Dificuldade"
    )

    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"
        ordering = ['nome']

    def __str__(self):
        return self.nome

