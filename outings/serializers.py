
from accounts.models import Account
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Outing
from accounts.serializers import PetSerializer
from accounts.models import Pet

class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = ['first_name', 'last_name']

class OutingSerializer(serializers.ModelSerializer):
    pet_ids = serializers.PrimaryKeyRelatedField(many=True) 
    # user_account = AccountSerializer()

    class Meta:
        model = Outing
        fields = ['id', 'start_time', 'end_time', 'created', 'pet_ids']

    def create(self, validated_data):
        print("create:", validated_data)
        outing = Outing.objects.create(**validated_data)
        for pet in validated_data['pets']:
            outing.pets.add(Pet.objects.get(id=pet))


        

