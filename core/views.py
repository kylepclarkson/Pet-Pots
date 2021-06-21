
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from .serializers import AccountSerializer, PetReadSerializer, PetWriteSerializer
from .models import Account, Pet


class PetViewSet(viewsets.ModelViewSet):
    """
    Pet View Set 
    """
    permission_classes = [ 
        permissions.IsAuthenticated,
    ]
    serializer_class = PetWriteSerializer
    
    def get_queryset(self):
        """ Filter by only the user's pets. """
        user = self.request.user
        return Pet.objects.filter(owner=user.user_account)

    def get_serializer_class(self):
        if self.action in ['create']:
            return PetWriteSerializer
        else:
            return PetReadSerializer

    def create(self, request, *args, **kwargs):
        """
        Create new pet instance for this user.
        """
        serializer = self.get_serializer_class()(data=request.data.pop('pet'))
        if serializer.is_valid():
            pet = serializer.save(owner=self.request.user.user_account)           
            return Response(PetReadSerializer(pet, context={'request': request}).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class AppointmentViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def create(self, request, *args, **kwargs):
        pass

