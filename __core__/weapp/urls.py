from django.urls import path
from django.contrib.auth import views as standart_views

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.index, name = 'index'),
]