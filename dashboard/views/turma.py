from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.models import Turma
from dashboard.filters import TurmaFilter
from django.core.paginator import Paginator

@login_required
def show_page(request):
    context = {}

    eFilter = TurmaFilter(
        request.GET,
        queryset=request.user.turmas.all()
    )
    context['eFilter'] = eFilter

    paginated_eFilter = Paginator(eFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_eFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'turma/turma_list.html', context=context)

class TurmaCreate(CreateView, LoginRequiredMixin):
    model = Turma
    fields = ['codigo', 'descricao', 'escola']
    success_url = '/dashboard/turmas'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TurmaDetail(DetailView, LoginRequiredMixin):
    model = Turma

@login_required
def delete(request, codigo):
    formObject = request.user.turmas.get(pk=codigo)
    formObject.delete()
    return redirect('turmas-list')