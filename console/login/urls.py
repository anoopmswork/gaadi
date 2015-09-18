from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import LoginView, CarView, VariantView
from . import views

urlpatterns = [
    url(r'^login', LoginView.as_view()),
    url(r'^dashboard', login_required(views.LoginView().dashboard), name='dashboard'),
    url(r'^logout', views.LoginView().logout, name='logout'),
    url(r'^cardetails', login_required(CarView.as_view())),
    url(r'^cars', login_required(views.CarView().list_cars), name='cars'),
    url(r'^deletecar', login_required(
        views.CarView().delete_cars), name='deletecars'),
    url(r'^specificcar', login_required(
        views.CarView().specific_car), name='specificcar'),
    url(r'^editcar', login_required(views.CarView().edit_car), name='editcar'),
    url(r'^addvariant', login_required(VariantView.as_view()), name='addvariant'),
    url(r'^listcars', login_required(views.VariantView().specific_cars), name='listcars'),
    url(r'^', LoginView.as_view()),
]
