from django.contrib import admin
from RNG.models import Users, Game
from django.contrib.auth.models import User, Group


# Register your models here.

admin.site.register(Users)
admin.site.register(Game)