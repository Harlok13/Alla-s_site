from django.urls import path
from main import views
from main.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', show_category, name='category'),
    path('aboutme/', about_me, name='about_me'),
    path('practice/', practice, name='practice'),
    path('articles/', articles, name='articles'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration')
]
