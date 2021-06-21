
from rest_framework import serializers

from .models import Outing, Pet
from accounts.serializers import AccountSerializer


class PetSerializer(serializers.ModelSerializer):

    avatar_thumbnail = serializers.SerializerMethodField()
    user_account = AccountSerializer()

    class Meta:
        model = Pet
        fields = '__all__'
        depth=1

    def get_avatar_thumbnail(self, pet):
        # Get url for avatar thumbnail.
        request = self.context.get('request')
        print("pet here", pet)
        avatar_url = pet.avatar_thumbnail.url
        return request.build_absolute_uri(avatar_url)
        
class OutingSerializer(serializers.ModelSerializer):

    # pets = PetSerializer()
    class Meta:
        model = Outing
        fields = '__all__'
        # Set depth to 1 to access fields of user_account instead of its pk. 
        depth=1


{
                "id": 1,
                "name": "Molly",
                "breed": "Yellow Lab",
                "description": "Eats a lot.",
                "avatar": "http://localhost:8000/media_dev/pets/pet_avatar_512_512.png",
                "user_account": 1
            }