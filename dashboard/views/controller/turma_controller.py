from dashboard.models import Turma, Habilidade
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def concluir(request, codigo):
    turma = request.user.turmas.get(pk=codigo)
    for d in turma.disciplinas.all():
        for a in turma.alunos.all():
            a.habilidades.add(*d.habilidades_ofertadas.all())
    turma.delete()
    return redirect('turmas-list')