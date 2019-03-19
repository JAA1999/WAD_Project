import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RNG_project.settings')
import django
django.setup()
from RNG.models import Category, Game, Rating, User
def populate():
    #creates a list of dictionaries containing games to add into each category
    action=[
        {"id": "AC2",
        "name": "Assassin's Creed 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"id": "GTAV",
        "name": "Grand Theft Auto V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"id": "DISH",
        "name": "Dishonored",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    rpg=[
        {"id": "SKY",
        "name": "Skyrim",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15},
        {"id": "ME2",
        "name": "Mass Effect 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15},
        {"id": "DAI",
        "name": "Dragon Age: Inquisition",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    strategy=[
        {"id": "DOTA2",
        "name": "DOTA 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 16},
        {"id": "CIV5",
        "name": "Civilization V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"id": "SPORE",
        "name": "Spore",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    puzzle=[
        {"id": "PORTAL2",
        "name": "Portal 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"id": "TTP",
        "name": "The Talos Principle",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"id": "THEWITNESS",
        "name": "The Witness",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    sports=[
        {"id": "ROCKETLEAGUE",
        "name": "Rocket League",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"id": "FIFA19",
        "name": "Fifa 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"id": "NBA2K19",
        "name": "NBA 2K19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3}
    ]
    mmo=[
        {"id": "WoW",
        "name": "World Of Warcraft",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"id": "ESO",
        "name": "Elder Scrolls Online",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"id": "GW2",
        "name": "Guild Wars 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    simulation=[
        {"id": "SIMS4",
        "name": "The Sims 4",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"id": "KSP",
        "name": "Kerbal Space Program",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"id": "FS19",
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
        c=add_cat(cat, cats[cat]["views"]["likes"])
        for p in cat_data["games"]:
            add_game(c,p["name"],p["url"],p["views"])
    for c in Category.objects.all():
        for p in Game.objects.filter(category=c):
            print("- {0} - {1}".format(str(c),str(p)))

    def add_game(cat, title, url, views):
        p = Game.objects.get_or_create(category=cat,title=title)[0]
        p.url = url
        p.views = views
        p.save()
        return p

    def add_cat(name,views,likes):
        c=Category.objects.get_or_create(name=name)[0]
        c.views=views
        c.likes=likes
        c.save()
        return c

    if __name__ == '__main__':
        print("*** Starting RNG population script ***")
        populate()
