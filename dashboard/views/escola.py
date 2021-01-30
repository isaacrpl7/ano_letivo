from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect
from django.shortcuts import render
from dashboard.models import Escola
from dashboard.filters import EscolaFilter
from django.core.paginator import Paginator

def show_page(request):
    context = {}

    eFilter = EscolaFilter(
        request.GET,
        queryset=Escola.objects.all()
    )
    context['eFilter'] = eFilter

    paginated_eFilter = Paginator(eFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_eFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'escola/escola_list.html', context=context)

class EscolaCreate(CreateView):
    model = Escola
    fields = ['codigo', 'descricao']
    success_url = '/dashboard/escolas'

def delete(request, codigo):
    formObject = Escola.objects.get(pk=codigo)
    formObject.delete()
    return redirect('escolas-list')