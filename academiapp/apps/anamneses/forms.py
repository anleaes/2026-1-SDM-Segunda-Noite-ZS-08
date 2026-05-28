from django import forms
from .models import Anamnese

class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese
        exclude = ()