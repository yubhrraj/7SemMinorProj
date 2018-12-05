from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    user = models.OneToOneField(User)
    key = models.CharField(max_length= 32, default="")

    def __str__(self):
        return self.user.username
   

    



