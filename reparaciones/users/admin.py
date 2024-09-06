from django.contrib import admin
from .models import IdentificationType, User, Client

# Register your models here.

admin.site.register(IdentificationType)
admin.site.register(User)
admin.site.register(Client)