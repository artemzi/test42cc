from django.contrib import admin

from .models import CustomProfile, Update


admin.site.register(CustomProfile)
admin.site.register(Update)