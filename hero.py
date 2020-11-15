import random
class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.starting_health = 100
        self.current_health = starting_health


    def fight(self,opponent):
        winner = random.choice([hero1,opponent])
        print(winner.name,'has won!')
        


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Grace Hopper",200)
    hero2 = Hero('Brent Shierk')
    hero1.fight(hero2)
