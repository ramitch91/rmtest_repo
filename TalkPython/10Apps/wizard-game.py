import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print()
    print('-----------------------------')
    print('      WIZARD GAME APP')
    print('-----------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        SmallAnimal('Bat', 5),
        Creature('Tiger', 10),
        Dragon('Red Dragon', 100, 50, True),
        Dragon('Green Dragon', 75, 50, False),
        Dragon('Black Dragon', 150, 75, True),
        Wizard('Evil Wizard', 1000)
    ]
#    for creature in creatures:
#        print(f"{creature.name}: Level {creature.level}")

    hero = Wizard('Gandolf', 250)
#    print(f"{hero.name} is level {hero.level}")

    while True:
        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} "
              f"comes out of a foggy forest...")
        print()
        cmd = input("Do you [a] attack, [r] run away, [l] look around: ")
        if cmd.lower() == 'a':
            if hero.attack(active_creature):
                hero.level = hero.level + (active_creature.level * 5)
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover.... ")
                time.sleep(5)
                print()
                print("The wizard is back and revitalized")

        elif cmd.lower() == 'r':
            print(f'The wizard is unsure of his power and flees.')
        elif cmd.lower() == 'l':
            print(f"The wizard looks to see what creatures may be around.")
            for c in creatures:
                print(f"* A {c.name} at level {c.level}")
        else:
            print('OK, goodbye.....exiting game')
            break

        if len(creatures) == 0:
            print(f"{hero.name} has defeated all of the creatures.")
            break


if __name__ == '__main__':
    main()
