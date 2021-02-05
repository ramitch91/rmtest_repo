import random

class Creature():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Creature: {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        hero_roll = self.get_defensive_roll()
        print(f"The wizard {self.name} rolls a {hero_roll}...")
        creature_roll = creature.get_defensive_roll()
        print(f"{creature.name} rolls a {creature_roll}...")

        if hero_roll >= creature_roll:
            print(f"The wizard {self.name} easily triumphs over the {creature.name}")
            return True
        else:
            print(f"The wizard {self.name} is DEFEATED....")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scale_factor, breaths_fire):
        super(Dragon, self).__init__(name, level)
        self.scale_factor = scale_factor
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scale_factor / 10
        return base_roll * fire_modifier * scale_modifier