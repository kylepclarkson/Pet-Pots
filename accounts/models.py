from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Account(models.Model):
    """ An account of a user """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="accounts/avatars/", default='accounts/account_avatar_512_512.jpg')
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(64,64)],
        format='jpeg',
        options={'quality': 70}
    )    
    

class Pet(models.Model):
    """ A pet of a user. """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
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
