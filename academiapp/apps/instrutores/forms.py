from django import forms
from .models import Instrutor

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        exclude = ()