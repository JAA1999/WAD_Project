from django.db import models

# Database Objects

class User(models.Model):
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

class Game(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    name = models.CharField(max_length = 64)
    user_score = models.FloatField()
    num_user_ratings = models.IntegerField()
    critic_score = models.FloatField()
    num_critic_ratings = models.IntegerField()
    age_rating = models.CharField(max_length = 4)
    description = models.TextField()

    # might need list[fk] for ratings


class Rating(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    score = models.FloatField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)