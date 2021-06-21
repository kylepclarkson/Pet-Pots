
from rest_framework import routers

from . import views

urlpatterns = []

router = routers.DefaultRouter()
router.register('appointments', views.AppointmentViewSet, 'appointments')
router.register('pets', views.PetViewSet, 'pets')

urlpatterns += router.urls