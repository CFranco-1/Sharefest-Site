from django.contrib import admin
from .models import AllUser, ContactModel

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(AllUser)