from django.db import models
from django.db.models import Avg
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

# TODO:
# Should add manage.py command to create groups
# Set group permissions for critics and reg users
# use clean() to make sure user is in correct group according to critic bool
# call this command in the pop script
# https://stackoverflow.com/questions/22250352/programmatically-create-a-django-group-with-permissions

# Database Objects
# Remember to migrate!
# Use python manage.py migrate --run-syncdb


class UserProfile(AbstractUser):
    # AbstractUser relevant fields:
    # username, password, first_name, last_name, date_joined, email, last_login

    critic = models.BooleanField(default=False)
    website = models.URLField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=64)
    # supercategory to allow hierarchical structure of categories
    supercategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'


class Game(models.Model):
    name = models.CharField(max_length=64)
    age_rating = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    is_approved = models.BooleanField(default=False)

    slug = models.SlugField(max_length=40)

    @property
    def avg_user_rating(self):
        return Rating.objects.filter(game='self', critic_rating=False).aggregate(Avg('score'))

    @property
    def avg_critic_rating(self):
        return Rating.objects.filter(game='self', critic_rating=True).aggregate(Avg('score'))

    @property
    def avg_rating(self):
        return Rating.objects.filter(game='self').aggregate(Avg('score'))

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    score = models.FloatField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    critic_rating = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def clean(self):
        # auto set critic rating by user
        if self.user:
            self.critic_rating = self.user.critic

    class Meta:
        # ensure only one rating per game per user
        unique_together = ('user', 'game',)


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)
    supercomment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        # auto get user's rating for game where comment is made
        if not self.rating:
            try:
                self.rating = Rating.objects.get(user=self.user, game=self.game)
            except Rating.DoesNotExist:
                ...

    def __str__(self):
        return '{} - {}'.format(self.game.name, str(self.user.username))

# import RNG.signals