
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Account

class RegisterSerializer(serializers.ModelSerializer):
    """ Register a new user """
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta: 
        model = User
        fields = ['id', 'username', 'password', 'password2', 'first_name', 'last_name']
        # exclude password from being read/displayed
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """ Register new user with valid credentials. Assumes that frontend
        had user confirmed their password. """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        # TODO send email to authenticated account.
        user_account = Account.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class LoginSerializer(serializers.Serializer):
    """ Serialize login attempt """
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        # Login attempt
        user = authenticate(**attrs)
        if not user:
            # User does not exist or invalid.
            raise serializers.ValidationError("Invalid login credentials")
        user_account = Account.objects.get(user=user)
        if not user_account.is_active:
            # User has not yet activated their account.
            raise serializers.ValidationError("Account is not yet activated. Please check your email.")

        return user

class AccountSerializer(serializers.ModelSerializer):
    # pets = PetSerializer(many=True)
    avatar_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_avatar_thumbnail(self, user):
        # Get url for avatar thumbnail.
        request = self.context.get('request')
        avatar_url = user.avatar_thumbnail.url
        return request.build_absolute_uri(avatar_url)

