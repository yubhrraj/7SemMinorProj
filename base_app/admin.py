from django.contrib import admin
from .models import AppUser, SecretKey

admin.site.register(AppUser)

admin.site.register(SecretKey)