"""
DESCRIPTION:
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.

Example:
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__
"""
import math
from operator import attrgetter


class Fighter:
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name, self.health, self.damage_per_attack
        )

    __repr__ = __str__


def declare_winner(fighter1: Fighter, fighter2: Fighter, first_attacker: str):
    first = fighter1 if fighter1.name == first_attacker else fighter2
    second = fighter2 if first.name == fighter1.name else fighter1
    result = get_winner(first, second)
    return result.name


def get_winner(fighter1, fighter2):
    fighter1_win_round = math.ceil(fighter1.health / fighter2.damage_per_attack)
    fighter2_win_round = math.ceil(fighter2.health / fighter1.damage_per_attack)

    if fighter1_win_round >= fighter2_win_round:
        return fighter1
    return fighter2


print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"))
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"))


def declare_winner_v2(fighter1: Fighter, fighter2: Fighter, first_attacker: str):
    fighter1.turns = math.ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = math.ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter("turns")).name


print(declare_winner_v2(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
print(declare_winner_v2(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"))
print(declare_winner_v2(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"))
