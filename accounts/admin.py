from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Account, Pet

class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'avatar_thumbnail')
    avatar_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'breed', 'avatar_thumbnail')
    avatar_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')

admin.site.register(Account, AccountAdmin)
admin.site.register(Pet, PetAdmin)
