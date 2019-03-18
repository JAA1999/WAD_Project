
from django.contrib import admin
from RNG.models import User, Game, Rating, Category, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(Comment)