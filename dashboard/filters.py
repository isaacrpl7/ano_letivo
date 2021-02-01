import django_filters
from .models import Escola, Turma, Aluno, Disciplina, Professor, Habilidade
from django_filters import NumberFilter

class EscolaFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Escola
        fields = '__all__'

class TurmaFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Turma
        fields = '__all__'

class AlunoFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Aluno
        fields = '__all__'

class DisciplinaFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Professor
        fields = '__all__'

class HabilidadeFilter(django_filters.FilterSet):
    codigo = NumberFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Habilidade
        fields = '__all__'