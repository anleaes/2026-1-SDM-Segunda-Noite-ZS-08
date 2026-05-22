from .models import Anamnese
from rest_framework import serializers

class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnese
        fields = [
            'aluno',
            'ultima_atualizacao',
            'alergias',
            'restricoes_fisicas',
            'medicamentos_em_uso',
            'pressao_arterial',
            'diabetes',
            'fumante',
            'problemas_cardiacos', 
            'cirurgias_recentes',
            'observacoes'
        ]