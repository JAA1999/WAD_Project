from django.db import models
from django.contrib.auth.models import User

# Database Objects

#Sign up doesnt work with this class so I've commented it out for now and used 
#the defaul django user model for regualr users and changed this to a critic model
class Critic(models.Model):
    # might use an ID integer as PK for more efficient sorting/searching
    username = models.CharField(max_length = 16, unique = True, primary_key = True)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    email = models.EmailField()     # might need additional parameters
	
    # password      need to setup password hasher etc
    critic = models.BooleanField()
    website = models.URLField(blank=True)    # not sure if optional is a param or if it is just left null
    description = models.TextField()

    # might need list[fk] for ratings

class UserProfile(models.Model):
	user =  models.OneToOneField(User)
	
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __str__(self):
		return self.user.username

class Game(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    name = models.CharField(max_length = 64)
    user_score = models.FloatField()
    num_user_ratings = models.IntegerField()
    critic_score = models.FloatField()
    num_critic_ratings = models.IntegerField()
    age_rating = models.CharField(max_length = 16)
    description = models.TextField()

    # might need list[fk] for ratings


class Rating(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    score = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)from django.db import models
from datetime import datetime

# Database Objects

class User(models.Model):
    # null/blank=True ensures the field is optional
    user =  models.CharField(max_length=16, unique=True, primary_key=True)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    critic = models.BooleanField()

    email = models.EmailField()
    website = models.URLField(null=True, blank=True)    
    description = models.TextField(null=True, blank=True)

    picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
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

    def __str__(self):
        return self.name

class Rating(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    score = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now(), blank = True)

    def __str__(self):
        return self.score

class Category(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(default=datetime.now(), blank = True)

    supercomment  = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.textfrom django.db import models
from datetime import datetime

# Database Objects

class User(models.Model):
    # null/blank=True ensures the field is optional
    user =  models.CharField(max_length=16, unique=True, primary_key=True)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    critic = models.BooleanField()

    email = models.EmailField()
    website = models.URLField(null=True, blank=True)    
    description = models.TextField(null=True, blank=True)

    picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
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

    def __str__(self):
        return self.name

class Rating(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    score = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now(), blank = True)

    def __str__(self):
        return self.score

class Category(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(default=datetime.now(), blank = True)

    supercomment  = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.text