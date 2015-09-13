from django.conf.urls import include, url
from django.contrib import admin
from .views import LoginView
from . import views

urlpatterns = [
    url(r'^login',LoginView.as_view()),
    url(r'^dashboard',views.LoginView.dashboard,name='dashboard'),
    url(r'^',LoginView.as_view()),
]