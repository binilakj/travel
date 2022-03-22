
from django.contrib import admin
from .models import photos
from .models import media

# Register your models here.
admin.site.register(photos)
admin.site.register(media)