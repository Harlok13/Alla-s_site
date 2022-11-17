from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'main/index.html')

def show_category(request):
    return HttpResponse('категории')

def show_post(request):
    return HttpResponse('пост')
