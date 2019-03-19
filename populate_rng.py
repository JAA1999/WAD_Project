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
        "age_rating": 15},
        {"ID": "ME2",
        "name": "Mass Effect 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15},
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
        "age_rating": 16},
        {"ID": "CIV5",
        "name": "Civilization V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"ID": "SPORE",
        "name": "Spore",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    puzzle=[
        {"ID": "PORTAL2",
        "name": "Portal 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"ID": "TTP",
        "name": "The Talos Principle",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"ID": "THEWITNESS",
        "name": "The Witness",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    sports=[
        {"ID": "ROCKETLEAGUE",
        "name": "Rocket League",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"ID": "FIFA19",
        "name": "Fifa 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"ID": "NBA2K19",
        "name": "NBA 2K19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3}
    ]
    mmo=[
        {"ID": "WoW",
        "name": "World Of Warcraft",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"ID": "ESO",
        "name": "Elder Scrolls Online",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"ID": "GW2",
        "name": "Guild Wars 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    simulation=[
        {"ID": "SIMS4",
        "name": "The Sims 4",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"ID": "KSP",
        "name": "Kerbal Space Program",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"ID": "FS19",
        "name": "Farming Simulator 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3}
    ]

    cats={"Action":{"games":action, "reviews":0},
        "RPG":{"games":rpg, "reviews":0},
        "Strategy":{"games":strategy, "reviews":0},
        "Puzzle":{"games":puzzle, "reviews":0},
        "Sports":{"games":sports, "reviews":0},
        "MMO":{"games":mmo, "reviews":0},
        "Simulation":{"games":simulation, "reviews":0},
    }

    for cat, cat_data in cats.items():
        c=add_cat(cat, cats[cat]["reviews"])
        for p in cat_data["games"]:
            add_game(c,p["name"],p["url"],p["reviews"])
    for c in Category.objects.all():
        for p in Game.objects.filter(category=c):
            print("- {0} - {1}".format(str(c),str(p)))

    def add_game(cat, title, url, reviews=0):
        p = Game.objects.get_or_create(category=cat,ID=ID)
        p.name=name
        p.user_score=user_score
        p.num_user_ratings=num_user_ratings
        p.critic_score=critic_score
        p.num_critic_ratings=num_critic_ratings
        p.age_rating=age_rating
        p.reviews=reviews
        p.save()
        return p

    def add_cat(name,views):
        c=Category.objects.get_or_create(name=name)[0]
        c.views=views
        c.save()
        return c

    if __name__ == '__main__':
        print("*** Starting RNG population script ***")
        populate()