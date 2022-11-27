from django.urls import path
from main import views
from main.views import *

# app_name = 'main'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', show_category, name='category'),
    path('aboutme/', about_me, name='about_me'),
    path('practices/', practices, name='practices'),
    path('articles/', articles, name='articles'),
    path('consultation/', consultation, name='consultation'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('post/<slug:post_slug>/', show_post, name='show_post')
]
