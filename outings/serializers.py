
from accounts.models import Account
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Outing

from accounts.serializers import PetSerializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = ['first_name', 'last_name']
        
class OutingSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True)
    user_account = AccountSerializer()

    class Meta:
        model = Outing
        fields = ['user_account', 'start_time', 'end_time', 'created', 'pets']

