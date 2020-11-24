import random
from Ability import Ability
from Armor import Armor
class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.starting_health = 100
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0


    def add_ability(self,ability):
        self.abilities.append(ability)
    
    def add_armor(self,armor):
        self.armors.append(armor)


    def attack(self):
        total_damgae = 0

        for ability in self.abilities:
            total_damgae += ability.attack()
        return total_damgae
    
    def defend(self):
        damage_amt = 0

        for armor in self.armors:
            damage_amt += armor.defend()
        return damage_amt
    
    def take_damage(self,damage_amt):
        self.current_health -= damage_amt + self.defend()
        if self.current_health < 0:
            self.current_health = 0
    
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills=1):
        self.kills += num_kills

    def add_death(self, num_deaths=1):
        self.deaths += num_deaths

    
    def fight(self, opponent):

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw".upper())
            return 0

        while self.is_alive() and opponent.is_alive():
            print(f"{self.name} attacked {opponent.name}")
            opponent.take_damage(self.attack())
            print(f"{opponent.name}'s remaining health: {opponent.current_health}")
            if opponent.is_alive():
                print(f"{opponent.name} attacked {self.name}")
                self.take_damage(opponent.attack())
                print(f"{self.name}'s remaining health: {self.current_health}")

        if not self.is_alive():
            opponent.add_kill(1)
            self.add_death(1)
            print(f"\n{self.name} has been killed by {opponent.name}\n".upper())
            return opponent.name
        elif not opponent.is_alive():
            opponent.add_death(1)
            self.add_kill(1)
            print(f"\n{opponent.name} has been killed by {self.name}\n".upper())
            return self.name




