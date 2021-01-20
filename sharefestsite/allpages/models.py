from django.db import models
from multi_email_field.fields import MultiEmailField
from django.db.models import Model
from django.contrib.auth import get_user_model

class ContactModel(models.Model):
    emails = MultiEmailField()

class AllUser(models.Model):
    title = models.CharField(verbose_name='title',max_length=30,null=True,blank=True)

    def __str__(self):
        return self.title