from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.IntroView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
]
