
from rest_framework import serializers

from .models import Pet, Appointment
from accounts.serializers import AccountSerializer


class PetSerializer(serializers.ModelSerializer):
    
    # id = serializers.IntegerField()
    class Meta:
        model = Pet
        fields = ['id', 'name', 'breed', 'bio']
        read_only_field = ['id']

    def create(self, validated_data):
        return super().create(validated_data)

class AppointmentSerializer(serializers.ModelSerializer):
    
    owner = AccountSerializer(required=False)
    walker = AccountSerializer(allow_null=True, required=False)
    pet = PetSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'owner', 'walker', 'pet', 'start_time', 'created']

    def update(self, instance, validated_data):
        print("appointment read update called")

        print("instance: \n", instance)
        print("validated_data: \n", validated_data)

        return super().update(instance, validated_data)
