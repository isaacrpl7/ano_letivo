from django.views.generic import UpdateView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.models import Aluno, Habilidade
from django.contrib import messages
from dashboard.forms import HabilidadeForm

def comparar_habilidades(obj, turma, request):
    # compara as habilidades
    habs = Habilidade.objects.none() # habilidades da turma
    if turma == None:
        return False
    for d in turma.disciplinas.all(): # percorre as disciplinas da turma
        habs |= d.habilidades_requeridas.all() # adicionar as habilidades requeridas de cada disciplina na lista
        
    for t_h in habs: # percorre as habilidades da turma
        aux = 0
        if obj == None:
            messages.add_message(request, messages.ERROR, 'Aluno não possui os requerimentos necessários!')
            return True
        for a_h in obj.habilidades.all(): # percorre as habilidades do aluno
            if a_h == t_h: # se o aluno tem a habilidade, entao o aux é 1, e ele continua o for
                aux = 1
        if(aux == 0): # se o aluno nao tem a habilidade, entao finaliza o for e retorna verdadeiro
            messages.add_message(request, messages.ERROR, 'Aluno não possui os requerimentos necessários!')
            return True
    # Se o for finalizar, retorna falso, pois o aluno tem as habilidades
    return False

@login_required
def removerhabilidade(request, hab, aluno):
    obj = request.user.alunos.get(pk=aluno) # aluno que terá sua habilidade removida
    habilidade = request.user.habilidades.get(pk=hab) # habilidade a ser removida do aluno
    obj.habilidades.remove(habilidade)
    if comparar_habilidades(obj, obj.turma, request): # compara novamente as habilidades com a turma, caso nao tenha, sai da turma
        obj.turma=None
        obj.save()
    return redirect('alunos-detail', aluno)

class AlunoMatricula(UpdateView, LoginRequiredMixin):
    model = Aluno
    fields = ['turma']
    success_url = '/alunos'

    def form_valid(self, form):
        form.instance.user = self.request.user
        if comparar_habilidades(self.object, form.instance.turma, self.request):
            return redirect('alunos-detail', self.object.codigo)
        return super().form_valid(form)
    
def adicionarHabilidades(request, aluno):
    aluno_object = Aluno.objects.get(codigo=aluno)
    if request.method == 'POST':
        form = HabilidadeForm(request.POST)
        if form.is_valid():
            habilidades = form.cleaned_data.get('habilidades') # retorna as habilidades selecionadas no formulário
            for codigo in habilidades:
                hab = Habilidade.objects.get(codigo=codigo) # habilidade com aquele código
                aluno_object.habilidades.add(hab) # adicione aquela habilidade no aluno
            return redirect('alunos-detail', aluno)
    else:
        form = HabilidadeForm()
        
    return render(request, 'aluno/aluno_habs.html', {'form': form, 'aluno': aluno_object})