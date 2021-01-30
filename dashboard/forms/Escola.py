from django import forms
from dashboard.models import Escola

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ('codigo', 'descricao')
        labels = {
            'codigo': 'Código',
            'descricao': 'Descrição'
        }