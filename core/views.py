
# from rest_framework import viewsets, permissions
# from rest_framework.response import Response

# from .serializers import OutingSerializer, PetSerializer
# from .models import Account, Pet

# class OutingViewSet(viewsets.ModelViewSet):
#     """ View set handles CRUD operations for Outing model. """
#     # API testing note. Header form: 
#     #       Authorization: Token 62fa4c38c4c778069f1b7ab7cf32e7dc5ff13a867d4ad5e8e3c54c852c31e4a1

#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]

#     serializer_class = OutingSerializer

#     def get_queryset(self):
#         """ Get outings for this user """
#         user_account = self.request.user.user_account
#         return Outing.objects.filter(user_account=user_account)

#     def list(self, request, *args, **kwargs):
#         print("list called")
#         return super().list(request, *args, **kwargs)

#     def retrieve(self, request, *args, **kwargs):
#         print("retrieve called")
#         return super().retrieve(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         print('update called')
#         print("pets:", request.data.get('pets'))
#         # updated nested pets
#         outing = Outing.objects.get(id=request.data.get('id'))
#         print("outing:", outing)
#         for pet in outing.pets.all():
#             outing.pets.remove(pet.get('id'))
#         for pet in request.data.get('pets'):
#             outing.pets.add(pet.get('id'))

#         serializer = PetSerializer(outing)
#         # return Response(serializer.data)
#         return super().update(request, *args, **kwargs)


#     def create(self, request, *args, **kwargs):
#         print('Request data', request.data)
#         print('Request user', self.request.user.user_account)
#         outing = Outing.objects.create(
#             user_account=self.request.user.user_account,
#             start_time=request.data['start_time'],
#             end_time=request.data['end_time'],
#         )

#         outing.save()
#         # Add pets
#         for pet in request.data['pets']:
#             print('pet: ', pet)
#             outing.pets.add(Pet.objects.get(id=pet['id']))

#         serializer = PetSerializer(outing)
#         return Response(serializer.data)


# class PetViewSet(viewsets.ModelViewSet):
#     serializer_class = PetSerializer

#     def get_queryset(self):
#         user_account = self.request.user.user_account
#         return Pet.objects.filter(user_account=user_account)
#         user_account = self.request.user.user_account
#         return Pet.objects.filter(user_account=user_account)