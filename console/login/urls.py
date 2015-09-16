from django.conf.urls import include, url
from django.contrib import admin
from .views import LoginView, CarView
from . import views

urlpatterns = [
    url(r'^login', LoginView.as_view()),
    url(r'^dashboard', views.LoginView().dashboard, name='dashboard'),
    url(r'^logout', views.LoginView().logout, name='logout'),
    url(r'^cardetails', CarView.as_view()),
    url(r'^cars', views.CarView().list_cars, name='cars'),
    url(r'^deletecar', views.CarView().delete_cars, name='deletecars'),
    url(r'^', LoginView.as_view()),
]
