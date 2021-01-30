from django.shortcuts import render, redirect

def show_page(request):
    context = {}

    return render(request, 'initial.html', context=context)