from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.filters import DisciplinaFilter
from dashboard.models import Disciplina
from django.core.paginator import Paginator

@login_required
def show_page(request):
    context = {}

    aFilter = DisciplinaFilter(
        request.GET,
        queryset=request.user.disciplinas.all()
    )
    context['aFilter'] = aFilter

    paginated_myFilter = Paginator(aFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_myFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'disciplina/disciplina_list.html', context=context)

class DisciplinaCreate(LoginRequiredMixin, CreateView):
    model = Disciplina
    fields = ['codigo', 'nome', 'descricao', 'turma']
    success_url = '/disciplinas'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DisciplinaUpdate(UpdateView, LoginRequiredMixin):
    model = Disciplina
    fields = ['codigo', 'nome', 'descricao', 'turma']
    success_url = '/disciplinas'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DisciplinaDetail(DetailView, LoginRequiredMixin):
    model = Disciplina

@login_required
def delete(request, codigo):
    formObject = request.user.disciplinas.get(pk=codigo)
    formObject.delete()
    return redirect('disciplinas-list')