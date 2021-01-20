from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfileManager(models.Manager):
    pass

class UserProfile(models.Model):
    userI = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=30)
    email = models.EmailField(default="")
    phone_num = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
    