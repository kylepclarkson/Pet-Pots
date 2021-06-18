
from rest_framework import viewsets, permissions, generics, views
from rest_framework.response import Response
from knox.models import AuthToken

from . import serializers
from .models import Account

class RegisterUserAPI(generics.GenericAPIView):
    """ Register new user """
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        # register new user and create (deactivate) account.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            # 'user': serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            'message': 'Account created! Please check your email for the activation link.'
        })
        

class LoginUserAPI(generics.GenericAPIView):
    """ Login existing user """
    serializer_class = serializers.LoginSerializer
    
    def post(self, request):
        """ Validate login attempt. If valid return account for user. """ 
        serializer = self.get_serializer(data=request.data)
        # validate
        serializer.is_valid(raise_exception=True)
        # Generate auth token
        user = serializer.validated_data
        print("Getting account")
        account = Account.objects.get(user=user)
        
        return Response({
            'account': serializers.AccountSerializer(account, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })
