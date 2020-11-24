from random import randint
from ability import Ability


class Spell(Ability):

    def attack(self):
        if randint(1, 10) > 8:
            return self.max_damage
        else:
            return 0