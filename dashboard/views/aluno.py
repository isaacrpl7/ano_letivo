from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.filters import AlunoFilter
from dashboard.models import Aluno
from django.core.paginator import Paginator

@login_required
def show_page(request):
    context = {}

    aFilter = AlunoFilter(
        request.GET,
        queryset=request.user.alunos.all()
    )
    context['aFilter'] = aFilter

    paginated_myFilter = Paginator(aFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_myFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'aluno/aluno_list.html', context=context)

class AlunoCreate(LoginRequiredMixin, CreateView):
    model = Aluno
    fields = ['codigo', 'nome', 'descricao', 'turma']
    success_url = '/dashboard/alunos'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def delete(request, codigo):
    formObject = request.user.alunos.get(pk=codigo)
    formObject.delete()
    return redirect('alunos-list')