from django import forms
from dashboard.models import Habilidade

class HabilidadeForm(forms.Form):
        OPTIONS = [(option.codigo, option ) for option in Habilidade.objects.all()]
        habilidades = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=OPTIONS, required=False)