from django.db import models
from django.utils import timezone
import uuid

from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


# Database Objects
# Remember to migrate!

# ID refs should autogenerate

class User(models.Model):
    username = models.CharField(max_length = 16, unique = True, primary_key = True)
    password = models.CharField(max_length = 32)    # uses password hasher in the forms.py
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    critic = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
	
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)
	
    def __str__(self):
         return self.username

class Category(models.Model):
    name = models.CharField(max_length=64)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 64)

    user_score = models.FloatField()
    num_user_ratings = models.IntegerField()
    critic_score = models.FloatField()
    num_critic_ratings = models.IntegerField()

    age_rating = models.CharField(max_length = 16)
    description = models.TextField()
    releasedate = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, blank = True)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, blank = True)

    supercomment = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
	
