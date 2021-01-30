import django_filters
from .models import Escola, Aluno
from django_filters import NumberFilter

class EscolaFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Escola
        fields = '__all__'

class AlunoFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Aluno
        fields = '__all__'