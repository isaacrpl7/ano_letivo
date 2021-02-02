from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dashboard.models import Escola
from dashboard.filters import EscolaFilter
from django.core.paginator import Paginator

@login_required
def show_page(request):
    context = {}

    eFilter = EscolaFilter(
        request.GET,
        queryset=request.user.escolas.all()
    )
    context['eFilter'] = eFilter

    paginated_eFilter = Paginator(eFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_eFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'escola/escola_list.html', context=context)

class EscolaCreate(CreateView, LoginRequiredMixin):
    model = Escola
    fields = ['codigo', 'nome', 'descricao']
    success_url = '/escolas'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EscolaUpdate(UpdateView, LoginRequiredMixin):
    model = Escola
    fields = ['codigo', 'nome', 'descricao']
    success_url = '/escolas'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EscolaDetail(DetailView, LoginRequiredMixin):
    model = Escola

@login_required
def delete(request, codigo):
    formObject = request.user.escolas.get(pk=codigo)
    formObject.delete()
    return redirect('escolas-list')