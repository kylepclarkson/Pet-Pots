from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from . import views

urlpatterns = [
    path('', views.IndexAPI.as_view()),
    path('auth/', include('knox.urls')),
    path('auth/register', views.RegisterUserAPI.as_view()),
    path('auth/login', views.LoginUserAPI.as_view()),
]