from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = []

router = routers.DefaultRouter()
router.register('', views.OutingViewSet, 'outings')

urlpatterns += router.urls