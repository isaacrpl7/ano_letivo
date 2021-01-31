from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    form = UserCreationForm(request.POST) # retorna o formulário para criação de novo usuário
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'registration/signup.html', {
        'form': form
    })