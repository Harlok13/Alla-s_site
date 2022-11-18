from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from main.models import Posts


def home_page(request):
    posts = Posts.objects.all()
    post_limit = Posts.objects.all()[:2]
    context = {
        'title': 'Главная страница',
        'posts': posts,
        'post_limit': post_limit
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

def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {  # эти параметры мы передаем в html файл
        'post': post,
        'title': post.title,
    }

    return render(request, 'main/post.html', context=context)
