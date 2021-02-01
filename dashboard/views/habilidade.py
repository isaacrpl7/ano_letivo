from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.filters import HabilidadeFilter
from dashboard.models import Habilidade
from django.core.paginator import Paginator

@login_required
def show_page(request):
    context = {}

    aFilter = HabilidadeFilter(
        request.GET,
        queryset=request.user.habilidades.all()
    )
    context['aFilter'] = aFilter

    paginated_myFilter = Paginator(aFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_myFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'habilidade/habilidade_list.html', context=context)

class HabilidadeCreate(LoginRequiredMixin, CreateView):
    model = Habilidade
    fields = ['codigo', 'nome', 'descricao', 'alunos']
    success_url = '/dashboard/habilidades'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def delete(request, codigo):
    formObject = request.user.habilidades.get(pk=codigo)
    formObject.delete()
    return redirect('habilidades-list')