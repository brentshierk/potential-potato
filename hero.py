import random
from Ability import Ability
from Armor import Armor
class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.starting_health = 100
        self.current_health = starting_health
        self.abilities = list()
        self.armours = list()


    def fight(self,hero,opponent):
        winner = random.choice([hero,opponent])
        print(winner.name,'has won!')

    def add_ability(self,ability):
        self.abilities.append(ability)
    
    def add_armor(self,armor):
        self.armours.append(armor)


    def attack(self):
        total_damgae = 0

        for ability in self.abilities:
            total_damgae += ability.attack()
        return total_damgae
    
    def defend(self,damage_amt):
        damage_amt = 0

        for armor in self.armours:
            damage_amt += armor.defend()
        return damage_amt





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())