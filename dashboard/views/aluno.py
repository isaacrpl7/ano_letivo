from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from dashboard.filters import AlunoFilter
from dashboard.models import Aluno
from django.core.paginator import Paginator

def show_page(request):
    context = {}

    aFilter = AlunoFilter(
        request.GET,
        queryset=Aluno.objects.all()
    )
    context['aFilter'] = aFilter

    paginated_myFilter = Paginator(aFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_myFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'aluno/aluno_list.html', context=context)

class AlunoCreate(CreateView):
    model = Aluno
    fields = ['codigo', 'descricao']
    success_url = '/dashboard/alunos'

def delete(request, codigo):
    formObject = Aluno.objects.get(pk=codigo)
    formObject.delete()
    return redirect('alunos-list')