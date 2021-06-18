
from rest_framework import serializers

from .models import Outing, Pet

class OutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outing
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = '__all__'

    def get_avatar_thumbnail(self, pet):
        # Get url for avatar thumbnail.
        request = self.context.get('request')
        avatar_url = pet.avatar_thumbnail.url
        return request.build_absolute_uri(avatar_url)
        

