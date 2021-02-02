from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.filters import ProfessorFilter
from dashboard.models import Professor
from django.core.paginator import Paginator

@login_required
def show_page(request):
    context = {}

    aFilter = ProfessorFilter(
        request.GET,
        queryset=request.user.professores.all()
    )
    context['aFilter'] = aFilter

    paginated_myFilter = Paginator(aFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_myFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'professor/professor_list.html', context=context)

class ProfessorCreate(LoginRequiredMixin, CreateView):
    model = Professor
    fields = ['codigo', 'nome', 'descricao', 'disciplina']
    success_url = '/professores'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfessorUpdate(UpdateView, LoginRequiredMixin):
    model = Professor
    fields = ['codigo', 'nome', 'descricao', 'disciplina']
    success_url = '/professores'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def delete(request, codigo):
    formObject = request.user.professores.get(pk=codigo)
    formObject.delete()
    return redirect('professores-list')