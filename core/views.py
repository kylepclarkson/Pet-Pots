
from functools import partial
from accounts.serializers import AccountSerializer
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from .serializers import AppointmentSerializer, PetSerializer
from .models import Account, Appointment, Pet


class PetViewSet(viewsets.ModelViewSet):
    """
    Pet View Set 
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PetSerializer


    def get_queryset(self):
        """ Filter by only the user's pets. """
        user = self.request.user
        return Pet.objects.filter(owner=user.account)


    def create(self, request, *args, **kwargs):
        """
        Create new pet instance for this user.
        """
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            # Add user_account instance
            pet = serializer.save(owner=self.request.user.account)
            return Response(PetSerializer(pet, context={'request': request}).data, status=status.HTTP_201_CREATED)
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
        return Appointment.objects.filter(owner=user)


    def create(self, request, *args, **kwargs):
        appointment_serializer = self.get_serializer_class()(
            data=request.data.get('appointment'))
        pet_serializer = PetSerializer(
            data=request.data.get('appointment').get('pet'))

        # Validate inputs
        if appointment_serializer.is_valid():
            if pet_serializer.is_valid():
                # Add user_account instance
                appointment = appointment_serializer.create(
                    appointment_vd=appointment_serializer.validated_data,
                    pet_vd=pet_serializer.validated_data,
                    owner=self.request.user.user_account
                )
                return Response(AppointmentSerializer(appointment, context={'request': request}).data, status=status.HTTP_201_CREATED)
            else:
                return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        print("update appointment called")
        appointment_serializer = self.get_serializer_class()(data=request.data)
        print(repr(self.get_serializer_class()))
        user = request.data.get('owner').get('user')

        # Validate inputs
        if appointment_serializer.is_valid():
            # Add user_account instance
            appointment = appointment_serializer.update(
                appointment_vd=appointment_serializer.validated_data,
            )
            return Response(AppointmentSerializer(appointment, context={'request': request}).data, status=status.HTTP_201_CREATED)

        else:
            return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)


    def partial_update(self, request, *args, **kwargs):
        print("partial update called")

        # id = request.data.get('id')
        # walker = request.data.get('walker')
        
        serializer = AppointmentSerializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # try:
        #     walker_instance = Account.objects.get(pk=walker.get('id'))
        # except Account.DoesNotExist:
        #     walker_instance = None

        # appointment = Appointment.objects.get(pk=request.data.get('id'))
        # appointment.walker = walker_instance
        # appointment.save()
        # return Response(AppointmentReadSerializer(instance=appointment, context={'request': request}).data, status=status.HTTP_202_ACCEPTED)
        # return super().partial_update(request, *args, **kwargs)