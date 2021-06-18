
from rest_framework import routers

from . import views

urlpatterns = []

router = routers.DefaultRouter()
router.register('outings', views.OutingViewSet, 'outings')
router.register('pets', views.PetViewSet, 'pets')

urlpatterns += router.urls