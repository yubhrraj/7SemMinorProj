from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class AppUser(models.Model):
    user = models.OneToOneField(User)
    key = models.CharField(max_length= 32, default= '')

    def __str__(self):
        return self.user.username
   


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = AppUser.objects.create(user= kwargs['instance'])

post_save.connect(create_profile, sender=User)