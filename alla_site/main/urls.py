from django.urls import path
from main import views
from main.views import *

urlpatterns = [
    path("", home_page, name='home_page')
]
