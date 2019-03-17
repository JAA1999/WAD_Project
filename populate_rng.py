import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD_Project')
import django
django.setup()
from RNG.models import Category, Game, Rating, User
def populate():
    #creates a list of dictionaries containing games to add into each category
    games=[
        {"ID": "AC2",
        "name": "Assassin's Creed 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "GTAV",
        "name": "Grand Theft Auto V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "LoZBoTW",
        "name": "The Legend of Zelda: Breath of the Wild",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "CODMW2",
        "name": "Call of Duty: Modern Warfare 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "DISH",
        "name": "Dishonored",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]