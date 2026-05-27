from django.db import models
from alunos.models import Aluno

# Create your models here.
class Anamnese(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='anamnese')
    ultima_atualizacao = models.DateField(auto_now=True, verbose_name="Última Atualização")
    problemas_cardiacos = models.BooleanField(default=False, verbose_name="Problemas Cardíacos")
    cirurgias_recentes = models.BooleanField(default=False, verbose_name="Cirurgias Recentes")
    alergias = models.TextField(blank=True, null=True, verbose_name="Alergias")
    restricoes_fisicas = models.TextField(blank=True, null=True, verbose_name="Restrições Físicas")
    medicamentos_em_uso = models.TextField(blank=True, null=True, verbose_name="Medicamentos em Uso")
    pressao_arterial = models.CharField(max_length=50, blank=True, null=True, verbose_name="Pressão Arterial")
    diabetes = models.BooleanField(default=False, verbose_name="Diabetes")
    fumante = models.BooleanField(default=False, verbose_name="Fumante")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta:
        verbose_name = "Anamnese"
        verbose_name_plural = "Anamneses"
        ordering = ['-ultima_atualizacao']

    def __str__(self):
        return f"Anamnese do aluno: {self.aluno}"