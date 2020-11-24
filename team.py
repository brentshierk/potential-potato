from random import choice


class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def remove_all_heros(self):
        self.heroes = []

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} has been revived.")

    def attack(self, other_team):
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            chosen_hero = choice(living_heroes)
            chosen_opponent = choice(living_opponents)
            print(f"{chosen_hero.name} vs {chosen_opponent.name}".upper())
            winner = chosen_hero.fight(chosen_opponent)
            if winner == chosen_hero.name:
                living_opponents.remove(chosen_opponent)
            elif winner == chosen_opponent.name:
                living_heroes.remove(chosen_hero)
            else:
                break