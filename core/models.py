from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from accounts.models import Account

class Pet(models.Model):
    """ A pet of a user. """
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    bio = models.TextField()
    
    avatar = models.ImageField(upload_to="pets/avatars/", default='pets/pet_avatar_512_512.png')
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(64,64)],
        format='PNG',
        options={'quality': 70}
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Appointment(models.Model):
    """
    A scheduled time for a walker to take a pet for a walker.
    """
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owner')
    walker = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='walker', null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    created = models.DateTimeField(auto_created=True)

    def __str__(self) -> str:
        return f'{self.walker} walking {self.owner}\'s pet {self.pet}'
