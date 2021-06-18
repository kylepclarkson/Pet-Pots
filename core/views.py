
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import OutingSerializer, PetSerializer
from .models import Outing, Pet

class OutingViewSet(viewsets.ModelViewSet):
    """ View set handles CRUD operations for Outing model. """
    # API testing note. Header form: 
    #       Authorization: Token 62fa4c38c4c778069f1b7ab7cf32e7dc5ff13a867d4ad5e8e3c54c852c31e4a1

    permission_classes = [
        # permissions.IsAuthenticated,
    ]

    serializer_class = OutingSerializer

    def get_queryset(self):
        """ Get outings for this user """
        user_account = self.request.user.user_account
        return Outing.objects.filter(user_account=user_account)


    def create(self, request, *args, **kwargs):
        print(request.data)
        outing = Outing.objects.create(
            request.data['user_account'],
            request.data['start_time'],
            request.data['end_time'],
        )

        outing.save()

        for pet in request.data['pets']:
            print('pet: ', pet)
            outing.pets.add(Pet.objects.get(id=pet.id))

        serializer = PetSerializer(outing)
        return Response(serializer.data)


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer

    def get_queryset(self):
        return Pet.objects.all()
        user_account = self.request.user.user_account
        return Pet.objects.filter(user_account=user_account)