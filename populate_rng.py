import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RNG_project.settings')
import django
django.setup()
from RNG.models import Category, Game, Rating, User
def populate():
    #creates a list of dictionaries containing games to add into each category
    action=[
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
        {"ID": "DISH",
        "name": "Dishonored",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    rpg=[
        {"ID": "SKY",
        "name": "Skyrim",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "ME2",
        "name": "Mass Effect 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "DAI",
        "name": "Dragon Age: Inquisition",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    strategy=[
        {"ID": "DOTA2",
        "name": "DOTA 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "CIV5",
        "name": "Civilization V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "SPORE",
        "name": "Spore",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    puzzle=[
        {"ID": "PORTAL2",
        "name": "Portal 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "TTP",
        "name": "The Talos Principle",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "THEWITNESS",
        "name": "The Witness",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    sports=[
        {"ID": "ROCKETLEAGUE",
        "name": "Rocket League",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "FIFA19",
        "name": "Fifa 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "NBA2K19",
        "name": "NBA 2K19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    mmo=[
        {"ID": "WoW",
        "name": "World Of Warcraft",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "ESO",
        "name": "Elder Scrolls Online",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "GW2",
        "name": "Guild Wars 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    simulation=[
        {"ID": "SIMS4",
        "name": "The Sims 4",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "KSP",
        "name": "Kerbal Space Program",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"ID": "FS19",
        "name": "Farming Simulator 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]