from django.urls import path, include
from django.contrib import admin

from dashboard.views import escola, turma, aluno, disciplina, professor, habilidade, index
from dashboard.views.controller import turma_controller, aluno_controller

urlpatterns = [
    path('', index.show_page, name='index'),

    # ESCOLAS
    path('escolas', escola.show_page, name='escolas-list'),
    path('escolas/novo', escola.EscolaCreate.as_view(template_name="escola/escola_add.html"), name='escolas-add'),
    path('escolas/<str:pk>', escola.EscolaDetail.as_view(template_name="escola/escola_detail.html"), name='escolas-detail'),
    path('escolas/editar/<str:pk>', escola.EscolaUpdate.as_view(template_name="escola/escola_add.html"), name='escolas-update'),
    path('escolas/excluir/<str:codigo>', escola.delete, name='escolas-delete'),

    # TURMAS
    path('turmas', turma.show_page, name='turmas-list'),
    path('turmas/concluir/<str:codigo>', turma_controller.concluir, name='turmas-concluir'),
    path('turmas/novo', turma.TurmaCreate.as_view(template_name="turma/turma_add.html"), name='turmas-add'),
    path('turmas/<str:pk>', turma.TurmaDetail.as_view(template_name="turma/turma_detail.html"), name='turmas-detail'),
    path('turmas/editar/<str:pk>', turma.TurmaUpdate.as_view(template_name="turma/turma_add.html"), name='turmas-update'),
    path('turmas/excluir/<str:codigo>', turma.delete, name='turmas-delete'),

    # ALUNOS
    path('alunos', aluno.show_page, name='alunos-list'),
    path('alunos/adicionar-habilidades/<str:aluno>', aluno_controller.adicionarHabilidades, name='alunos-add-habilidade'),
    path('alunos/remover-habilidade/<str:hab>&<str:aluno>', aluno_controller.removerhabilidade, name='remover-habilidade'),
    path('alunos/novo', aluno.AlunoCreate.as_view(template_name="aluno/aluno_add.html"), name='alunos-add'),
    path('alunos/<str:pk>', aluno.AlunoDetail.as_view(template_name="aluno/aluno_detail.html"), name='alunos-detail'),
    path('alunos/editar/<str:pk>', aluno.AlunoUpdate.as_view(template_name="aluno/aluno_add.html"), name='alunos-update'),
    path('alunos/matricular/<str:pk>', aluno_controller.AlunoMatricula.as_view(template_name="aluno/aluno_matricula.html"), name='alunos-matricula'),
    path('escolas/excluir/<str:codigo>', escola.delete, name='alunos-delete'),

    # DISCIPLINAS
    path('disciplinas', disciplina.show_page, name='disciplinas-list'),
    path('disciplinas/novo', disciplina.DisciplinaCreate.as_view(template_name="disciplina/disciplina_add.html"), name='disciplinas-add'),
    path('disciplinas/<str:pk>', disciplina.DisciplinaDetail.as_view(template_name="disciplina/disciplina_detail.html"), name='disciplinas-detail'),
    path('disciplinas/editar/<str:pk>', disciplina.DisciplinaUpdate.as_view(template_name="disciplina/disciplina_add.html"), name='disciplinas-update'),
    path('disciplinas/excluir/<str:codigo>', disciplina.delete, name='disciplinas-delete'),

    # PROFESSORES
    path('professores', professor.show_page, name='professores-list'),
    path('professores/novo', professor.ProfessorCreate.as_view(template_name="professor/professor_add.html"), name='professores-add'),
    path('professores/editar/<str:pk>', professor.ProfessorUpdate.as_view(template_name="professor/professor_add.html"), name='professores-update'),
    path('professores/excluir/<str:codigo>', professor.delete, name='professores-delete'),

    # HABILIDADES
    path('habilidades', habilidade.show_page, name='habilidades-list'),
    path('habilidades/novo', habilidade.HabilidadeCreate.as_view(template_name="habilidade/habilidade_add.html"), name='habilidades-add'),
    path('habilidades/editar/<str:pk>', habilidade.HabilidadeUpdate.as_view(template_name="habilidade/habilidade_add.html"), name='habilidades-update'),
    path('habilidades/excluir/<str:codigo>', habilidade.delete, name='habilidades-delete'),
]