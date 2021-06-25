
from rest_framework import serializers

from .models import Pet, Appointment
from accounts.serializers import AccountReadSerializer, AccountWriteSerializer


class PetReadSerializer(serializers.ModelSerializer):
    """ Used when accessing existing instance. """
    id = serializers.IntegerField()
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
    owner = AccountReadSerializer()
    walker = AccountReadSerializer()
    owner = AccountReadSerializer(required=False)
    walker = AccountReadSerializer(required=False)
    pet = PetReadSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'owner', 'walker', 'pet', 'start_time', 'created']


class AppointmentWriteSerializer(serializers.ModelSerializer):
    """ Use when creating new instace. """
    owner = AccountWriteSerializer()
    walker = AccountWriteSerializer(required=False)
    pet = PetReadSerializer()

    class Meta:
        model = Appointment
        fields = ['pet', 'owner', 'walker', 'pet', 'start_time']

    def create(self, appointment_vd, pet_vd, owner):
        pet = Pet.objects.get(id=pet_vd.get('id'))
        appointment = Appointment.objects.create(owner=owner, pet=pet, start_time=appointment_vd.get('start_time'))
        return appointment

    def update(self, instance, validated_data):
        print('validated data', validated_data)
        return super().update(instance, validated_data)
