from django.urls import path, include
from django.contrib import admin

from dashboard.views import escola, aluno, index

urlpatterns = [
    path('', index.show_page, name='index'),

    # ESCOLAS
    path('escolas', escola.show_page, name='escolas-list'),
    path('escolas/novo', escola.EscolaCreate.as_view(template_name="escola/escola_add.html"), name='escolas-add'),
    # path('escolas/<int:pk>', escola.EscolaUpdate, name='escolas-update'),
    path('escolas/excluir/<int:codigo>', escola.delete, name='escolas-delete'),

    # ALUNOS
    path('alunos', aluno.show_page, name='alunos-list'),
    path('alunos/novo', aluno.AlunoCreate.as_view(template_name="aluno/aluno_add.html"), name='alunos-add'),

    path('escolas/excluir/<int:codigo>', escola.delete, name='alunos-delete'),

]