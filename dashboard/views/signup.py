from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    form = UserCreationForm(request.POST) # retorna o formulário para criação de novo usuário
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'registration/signup.html', {
        'form': form
    })