
from rest_framework import viewsets, permissions
from .serializers import OutingSerializer

from .models import Outing
from accounts.models import Account

class OutingViewSet(viewsets.ModelViewSet):
    """ View set handles CRUD operations for Outing model. """
    # API testing note. Header form: 
    #       Authorization: Token 62fa4c38c4c778069f1b7ab7cf32e7dc5ff13a867d4ad5e8e3c54c852c31e4a1
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = OutingSerializer

    def get_queryset(self):
        """ Get outings for this user """
        user_account = self.request.user.user_account
        print("User: ", user_account.user)
        return Outing.objects.filter(user_account=user_account)


    # def perform_create(self, serializer):
    #     print("perform create", self.request.user.user_account)
    #     serializer.save(user_account=self.request.user.user_account)