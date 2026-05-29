from django import forms
from .models import PlanosMensalidade

class PlanosMensalidadeForm(forms.ModelForm):
    class Meta:
        model = PlanosMensalidade
        exclude = ()