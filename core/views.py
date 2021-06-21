
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from .serializers import AppointmentReadSerializer, AppointmentWriteSerializer, PetReadSerializer, PetWriteSerializer
from .models import Account, Appointment, Pet


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
            # Add user_account instance
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

    def get_queryset(self):
        """ Filter by the creator of the appointment (pet owner) """
        user = self.request.user
        return Appointment.objects.filter(owner=user.user_account)

    def get_serializer_class(self):
        if self.action in ['create']:
            return AppointmentWriteSerializer
        else:
            return AppointmentReadSerializer


    def create(self, request, *args, **kwargs):
        appointment_serializer = self.get_serializer_class()(data=request.data.get('appointment'))
        pet_serializer = PetReadSerializer(data=request.data.get('appointment').get('pet'))
        
        # Validate inputs
        if appointment_serializer.is_valid():
            if pet_serializer.is_valid():
                # Add user_account instance
                appointment = appointment_serializer.create(
                    appointment_vd=appointment_serializer.validated_data,
                    pet_vd=pet_serializer.validated_data, 
                    owner=self.request.user.user_account
                )           
                return Response(AppointmentReadSerializer(appointment, context={'request': request}).data, status=status.HTTP_201_CREATED)
            else: 
                return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        else:
            return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

