from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Account(models.Model):
    """ An account of a user """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)

    avatar = models.ImageField(upload_to="accounts/avatars/", default='accounts/account_avatar_512_512.jpg')
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(64,64)],
        format='jpeg',
        options={'quality': 70}
    )    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'



