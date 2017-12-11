from django.contrib import admin

# Register your models here.

from .models import Installations, Meters, Channels

admin.site.register(Installations)
admin.site.register(Meters)
admin.site.register(Channels)