from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from . import views

urlpatterns = [
    path('', views.IndexAPI.as_view()),
    path('', include('knox.urls')),
    path('register', views.RegisterUserAPI.as_view()),
    path('login', views.LoginUserAPI.as_view()),
]