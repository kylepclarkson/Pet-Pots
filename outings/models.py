from django.db import models
from accounts.models import Account, Pet

class Outing(models.Model):
    """ A walking session where the user that creates it specifies a time they are available
    and other constraints. """
    # Creator of this Outing/walker
    user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    pets = models.ManyToManyField(Pet, blank=True)

    def __str__(self) -> str:
        return f'{self.user_account}: [{self.start_time} - {self.end_time}]'