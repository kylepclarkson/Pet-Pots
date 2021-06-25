from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from . import views

urlpatterns = [
    path('', include('knox.urls')),
    path('register', views.RegisterUserAPI.as_view(), name='auth-register'),
    path('login', views.LoginUserAPI.as_view(), name='auth-login'),
]

router = routers.DefaultRouter()

urlpatterns += router.urls