from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


# Database Objects

class Users(models.Model):
    # might use an ID integer as PK for more efficient sorting/searching
    username = models.CharField(max_length = 16, unique = True, primary_key = True)
    password = models.CharField(max_length = 32)    # uses password hasher in the forms.py
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    critic = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
	
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(default=datetime.now(), blank=True)
	
    def __str__(self):
         return self.username


class Game(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    name = models.CharField(max_length = 64)
    user_score = models.FloatField()
    num_user_ratings = models.IntegerField()
    critic_score = models.FloatField()
    num_critic_ratings = models.IntegerField()
    age_rating = models.CharField(max_length = 16)
    description = models.TextField()
    #need to add into pop script
    releasedate = models.DateField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    score = models.FloatField()
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(default=datetime.now(), blank = True)


class Category(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Comment(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(default=datetime.now(), blank = True)

    supercomment = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
	
