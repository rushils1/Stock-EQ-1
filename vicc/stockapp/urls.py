from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Home),
    path('untitled-1.html',views.Home),
    path('login.html',views.Login),
    path('register.html',views.Register),
    path('untitled.html',views.AboutUs),
    #path('index.html',views.Index),
    path('index.html',views.index),
    path('trial.html',views.index1),
    #path('search.html', views.stock_data),
]
