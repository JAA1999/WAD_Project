from django.db import models
from django.utils import timezone
import uuid

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Database Objects
# Remember to migrate!

# ID refs should autogenerate

class UserProfile(models.Model):
	
    user = models.OneToOneField(User)
    critic = models.BooleanField(default=False)
	
    website = models.URLField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    slug = models.SlugField(max_length=40)

    def __str__(self):
         return self.user.username

    def save(self, *args, **kwargs):
        self.slug=slugify(self.user.username)
        super(UserProfile,self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=64)
    supercategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=40)

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

    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Game, self).save(*args, **kwargs)

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
	
