
from rest_framework import viewsets, permissions
from .serializers import OutingSerializer

from .models import Outing

class OutingViewSet(viewsets.ModelViewSet):
    """ View set handles CRUD operations for Outing model. """

    permission_classes = [
        # permissions.IsAuthenticated
    ]

    serializer_class = OutingSerializer

    def get_queryset(self):
        # print("user_account", self.request.user_account)
        print("request: ", self.request.body)
        return Outing.objects.all()