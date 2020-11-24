from random import randint
from ability import Ability


class Weapon(Ability):

    def attack(self):
        return randint((self.max_damage // 2), self.max_damage)