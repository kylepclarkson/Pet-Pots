
from rest_framework import viewsets, permissions, generics, views, status
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.status import HTTP_200_OK

from . import serializers
from .models import Account

class RegisterUserAPI(generics.GenericAPIView):
    """ Register new user """
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        # register new user and create (deactivate) account.
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Create user and authentication token.
            user = serializer.save()
            return Response({
                'token': AuthToken.objects.create(user)[1]
            },
            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

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
            'account': serializers.AccountReadSerializer(account, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })
