import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RNG_project.settings')
import django
django.setup()
from RNG.models import Category, Game, Rating, UserProfile

import random
from string import ascii_lowercase  # for username

# TODO:
# randomly generate values for game fields
# generate ratings for games

def populate():
    #creates a list of dictionaries containing games to add into each category
    action=[
        {"name": "Assassin's Creed 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18,
        "description": "An action adventure game focussed on the story of Ezio Auditore da Firenze, an assassin, in Renaissance Italy.",
        "releasedate": "2009-11-17"},
        {"name": "Grand Theft Auto V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18,
        "description": "An open-world action game focussing on the lives of three criminals residing in Los Santos.",
        "releasedate": "2013-09-17"},
        {"id": "DISH",
        "name": "Dishonored",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18,
        "description": "An action adventure game set in an alternate dystopian Victorian England reality in which a bodyguard turned assassin seeks revenge on those who conspired against him.",
        "releasedate": "2012-10-09"}
    ]
    rpg=[
        {"name": "Skyrim",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15,
        "description": "An open-world role playing game set in the fictional world of Skyrim where dragons have mysteriously reappeared.",
        "releasedate": "2011-11-11"},
        {"name": "Mass Effect 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15,
        "description": "An open-world role playing game set far in the future where faster than light travel is common technology. Commander Shepard must face many enemies and moral dilemmas in his fight against the Collectors.",
        "releasedate": "2010-01-26"},
        {"id": "DAI",
        "name": "Dragon Age: Inquisition",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18,
        "description": "An open-world role playing game set in a demon-filled medieval world. The only way to save the world is to recreate the long forgotten inquisition.",
        "releasedate": "2014-11-18"}
    ]
    strategy=[
        {"name": "DOTA 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 16,
        "description": "A strategy game in which you have a selection of heroes, each taking hours to master, and fight in a team of six against the other team.",
        "releasedate": "2013-07-09"},
        {"name": "Civilization V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "A strategy game in which you create a civilization and develop it over millenia amongst other civilizations all aiming for victory.",
        "releasedate": "2010-09-21"},
        {"name": "Spore",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "A strategy game in which you create a single-celled organism that evolves over millenia into the world's dominant species.",
        "releasedate": "2008-09-04"}
    ]
    puzzle=[
        {"name": "Portal 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "A singleplayer/multiplayer puzzle game revolving around the use of a portal gun. Set in an abandoned laboratory populated by yourself and AI's.",
        "releasedate": "2011-04-18"},
        {"name": "The Talos Principle",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "A singleplayer puzzle game set in an empty robot-filled world.",
        "releasedate": "2014-12-11"},
        {"name": "The Witness",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "A singleplayer puzzle game set on a mysterious island.",
        "releasedate": "2016-01-26"}
    ]
    sports=[
        {"name": "Rocket League",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3,
        "description": "A sports game resembling football only with cars and exploding goals.",
        "releasedate": "2015-07-07"},
        {"name": "Fifa 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3,
        "description": "A sports game allowing you to take control in your very own footballing world.",
        "releasedate": "2018-09-28"},
        {"name": "NBA 2K19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3,
        "description": "A sports game allowing you to take control in your very own basketballing world.",
        "releasedate": "2018-09-07"}
    ]
    mmo=[
        {"name": "World Of Warcraft",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "An MMORPG featuring a huge expansive world with multiple choices for race and class along with near-infinite quests.",
        "releasedate": "2004-11-23"},
        {"name": "Elder Scrolls Online",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "An MMORPG featuring a huge expansive world with multiple choices for race and class along with near-infinite quests set in the same universe as Skyrim.",
        "releasedate": "2014-04-04"},
        {"name": "Guild Wars 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12,
        "description": "An MMORPG featuring a huge expansive world with multiple choices for race and class along with near-infinite quests.",
        "releasedate": "2012-08-28"}
    ]
    simulation=[
        {"name": "The Sims 4",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3,
        "description": "A simulation game in which you create an avatar and dictate it's life in the simulated world of Sims.",
        "releasedate": "2014-09-02"},
        {"name": "Kerbal Space Program",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3,
        "description": "A simulation game in which you build rockets to be piloted by strange minion-like creatures.",
        "releasedate": "2011-06-24"},
        {"name": "Farming Simulator 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3,
        "description": "A simulation game in which you own and manage a farm.",
        "releasedate": "2018-11-20"}
    ]

    # cats={"Action":{"games":action, "reviews":0},
    #     "RPG":{"games":rpg, "reviews":0},
    #     "Strategy":{"games":strategy, "reviews":0},
    #     "Puzzle":{"games":puzzle, "reviews":0},
    #     "Sports":{"games":sports, "reviews":0},
    #     "MMO":{"games":mmo, "reviews":0},
    #     "Simulation":{"games":simulation, "reviews":0},
    # }
    
    # maintained dict structure here in case we want to add supercategories
    cats = {"Action":action,
            "RPG":rpg,
            "Strategy":strategy,
            "Puzzle":puzzle,
            "Sports":sports,
            "MMO":mmo,
            "Simulation":simulation,
    }

    def generate_string(length):
        return "".join(random.choice(ascii_lowercase) for i in range(length))

    def generate_user(critic):
        username = generate_string(10)
        first_name = generate_string(10)
        last_name = generate_string(10)
        user = UserProfile.objects.get_or_create(username=username, first_name=first_name,
                                                 last_name=last_name)[0]
        user.save()
        return user

    def generate_rating(game, user):
        # generate random val between 1-10
        score = random.randint(1, 10)
        rating = Rating.objects.get_or_create(score=score, game=game, username=user,
                                              critic_rating=user.critic)[0]
        return rating

    def generate_comment():


    def add_game(cat, name, age_rating):
        # [0] specifies object in the [object, boolean created]
        game = Game.objects.get_or_create(category=cat, name=name, age_rating=age_rating)[0]
        game.save()
        return game

    def add_cat(name):
        c=Category.objects.get_or_create(name=name)[0]
        c.save()
        return c

    # for cat, cat_data in cats.items():
    #     c=add_cat(cat, cats[cat]["views"]["likes"])
    #     for p in cat_data["games"]:
    #         add_game(c,p["name"],p["url"],p["views"])
    
    for name, games in cats.items():
        cat = add_cat(name)
        for game in games:
            add_game(cat, name=game["name"], age_rating=game["age_rating"])
    
    for c in Category.objects.all():
        for p in Game.objects.filter(category=c):
            print("- {0} - {1}".format(str(c),str(p)))



if __name__ == '__main__':
    print("*** Starting RNG population script ***")
    populate()
