from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from accounts.models import Account

class Pet(models.Model):
    """ A pet of a user. """
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    
    description = models.TextField()
    
    avatar = models.ImageField(upload_to="pets/avatars/", default='pets/pet_avatar_512_512.png')
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(64,64)],
        format='PNG',
        options={'quality': 70}
    )

    def __str__(self) -> str:
        return f'{self.name}'

class Outing(models.Model):
    """ A walking session where the user that creates it specifies a time they are available
    and other constraints. """
    # Creator of this Outing/walker
    user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    pet_capacity = models.IntegerField(default=1)
    pets = models.ManyToManyField(Pet, blank=True)

    def __str__(self) -> str:
        return f'{self.user_account}: [{self.start_time} - {self.end_time}]'