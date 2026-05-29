from django import forms
from .models import PlanoAlimentar

class PlanoAlimentarForm(forms.ModelForm):
    class Meta:
        model = PlanoAlimentar
        fields = '__all__'
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }