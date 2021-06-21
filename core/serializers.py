
from rest_framework import serializers

from .models import Pet, Appointment
from accounts.serializers import AccountSerializer


class PetReadSerializer(serializers.ModelSerializer):
    """ Used when accessing existing instance. """
    
    class Meta:
        model = Pet
        fields = ['id', 'name', 'breed', 'bio']


class PetWriteSerializer(serializers.ModelSerializer):
    """ Use when creating new instace. """
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'bio']


class AppointmentReadSerializer(serializers.ModelSerializer):
    """ Used when accessing existing instance. """
    owner = AccountSerializer()
    walker = AccountSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'owner', 'walker', 'pet', 'start_time', 'created']


class AppointmentWriteSerializer(serializers.ModelSerializer):
    """ Use when creating new instace. """

    class Meta:
        model = Appointment
        fields = ['pet', 'end_time']

