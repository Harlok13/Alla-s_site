from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', context=context)

def show_category(request):
    return HttpResponse('категории')

def show_post(request):
    return HttpResponse('пост')

def about_me(request):
    return HttpResponse('обо мне')

def practices(request):
    return HttpResponse('мои практики')

def articles(request):
    return HttpResponse('мои статьи')

def login(request):
    return HttpResponse('вход')

def registration(request):
    return HttpResponse('регистрация')

def consultation(request):
    return HttpResponse('консультации')
