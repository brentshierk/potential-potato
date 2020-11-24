from ability import Ability
from weapon import Weapon
from spell import Spell
from armor import Armor
from hero import Hero
from team import Team
from random import choice

class Arena:

    def __init__(self):
        self.previous_winner = None

    def create_ability(self):
        
        name = ""
        while len(name) < 1:
            name = input("What is the ability name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the ability?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Ability(name, max_damage)

    def create_weapon(self):
        
        name = ""
        while len(name) < 1:
            name = input("What is the weapon name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the weapon?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Weapon(name, max_damage)

    def create_spell(self):
        
        name = ""
        while len(name) < 1:
            name = input("What is the spell name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the spell?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Spell(name, max_damage)

    def create_armor(self):
        
        name = ""
        while len(name) < 1:
            name = input("What is the armor name?  ")
        max_block = 0
        while max_block < 1:
            max_block = input("What is the max block of the armor?  ")
            try:
                max_block = int(max_block)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_block = 0
                print("Please enter a number.")
        return Armor(name, max_block)

    def create_hero(self):
        
        print("\n")
        hero_name = ""
        while len(hero_name) < 1:
            hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "5":
            add_item = input(
                "\n[1] Add ability\n[2] Add weapon\n[3] Add spell\n[4] Add armor\n[5] Done adding items\n\nYour choice: "
            )
            if add_item == "1":
                abilty = self.create_ability()
                hero.add_ability(abilty)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                spell = self.create_spell()
                hero.add_spell(spell)
            elif add_item == "4":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team(self, team):
        print("{:-^50}".format(team.name).upper())
        members = None
        while not isinstance(members, int):
            members = input(f"number of members on your team: {team.name}?\n")
            try:
                numOfTeamMembers = abs(int(members))
                team.remove_all_heros()
                for i in range(numOfTeamMembers):
                    hero = self.create_hero()
                    team.add_hero(hero)
                    print("\n")
                    print(f"{hero.name} has been added to {team.name}".upper())
                break
            except(ValueError, TypeError):
                print("Please enter a number.")
        print("\n")

    def authorize(self, team):
        print(
            "{:-^50}".format(f"{team.name} compleating authorization").upper()
        )
        for hero in team.heroes:
            if len(hero.abilities) == 0:
                print(f"{hero.name} is all clear for authorization")
            for ability in hero.abilities:
                if ability.max_damage > 100:
                    print(
                        f"{hero.name}'s {ability.name} is unauthorized for use"
                    )
                    hero.abilities.remove(ability)
                else:
                    print(
                        f"{hero.name}'s {ability.name} has been authorized for use"
                    )
            if len(hero.armors) == 0:
                print(f"{hero.name} has no armor to authorize")
            for armor in hero.armors:
                if armor.max_block > 100:
                    print(
                        f"{hero.name}'s {armor.name} is unauthorized for use"
                    )
                    hero.armors.remove(armor)
                else:
                    print(
                        f"{hero.name}'s {armor.name} has been authorized for use"
                    )
        print("\n")

    def team_battle(self, team_one, team_two):
        self.authorize(team_one)
        self.authorize(team_two)
        print("{:-^50}".format("FIGHT!"))
        team_one.attack(team_two)

    def surviving_heroes(self, team):
        survival_count = 0
        for hero in team.heroes:
            if hero.is_alive():
                print(f"{hero.name} has made it out of battle!")
                survival_count += 1
        if not survival_count:
            print("no heroes survived")
        return survival_count

    def winning_team(self, team_one, team_one_survival_count, team_two, team_two_survival_count):
        if team_one_survival_count and team_two_survival_count:
            print("{:-^50}".format("Draw!No winner could be choosen").upper())
            self.previous_winner = None
        elif team_one_survival_count:
            p = f"{team_one.name} won"
            print("{:=^50}".format(p).upper())
            self.previous_winner = team_one
        else:
            p = f"{team_two.name} won"
            print("{:=^50}".format(p).upper())
            self.previous_winner = team_two

    def kd_average(self, team):
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"average K/D: {team_kills/team_deaths}")

    def show_stats(self, team_one, team_two):
        print("\n")
        print("{:-^50}".format("STATS"))
        print("\n")
        print(f"{team_one.name} stats: ".upper())
        team_one_survival_count = self.surviving_heroes(team_one)
        self.kd_average(team_one)
        print("\n")
        print(f"{team_two.name} stats: ".upper())
        team_two_survival_count = self.surviving_heroes(team_two)
        self.kd_average(team_two)
        print("\n")
        self.winning_team(team_one, team_one_survival_count, team_two, team_two_survival_count)
        print("\n")


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()
    team_one = Team("Team One")
    team_two = Team("Team Two")

    print("\n")
    print("{:-^50}".format("WELCOME TO THE ARENA"))
    print("\n")

    reward_weapons = [
        Weapon("Big boots", 80),
        Weapon("Pillow", 63),
        Weapon("super bright flash light", 72),
        Weapon("Water gun", 92)
    ]

    arena.build_team(team_one)
    arena.build_team(team_two)

    while game_is_running:

        arena.team_battle(team_one, team_two)
        arena.show_stats(team_one, team_two)
        play_again = input("Play Again? Yes or No: ")

        if play_again.lower() == "n":
            game_is_running = False
        elif (play_again.lower() == "y"):

            team_one.revive_heroes()
            team_two.revive_heroes()

            try:
                chosen_hero = choice(arena.previous_winner.heroes)
                reward_weapon = choice(reward_weapons)
                chosen_hero.add_weapon(reward_weapon)
                print(
                    f"{chosen_hero.name} was rewarded with a {reward_weapon.name}"
                )
            except(AttributeError):
                pass

            edit_team = input("Edit your team? Yes or No: ")

            if edit_team.lower() == "y":
                arena.build_team(team_one)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team(team_one)
    arena.build_team(team_two)

    while game_is_running:

        arena.team_battle(team_one,team_two)
        arena.show_stats(team_one,team_two)
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            team_one.revive_heroes()
            team_two.revive_heroes()