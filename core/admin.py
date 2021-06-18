from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Outing, Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'breed', 'avatar_thumbnail')
    avatar_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')

admin.site.register(Outing)
admin.site.register(Pet, PetAdmin)
