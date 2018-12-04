from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    user = models.OneToOneField(User)

    # def __str__(self):
    #     return self.user.username
   

class SecretKey(models.Model):
    user = models.ForeignKey(AppUser, unique = True)
    key = models.CharField(max_length= 32)



