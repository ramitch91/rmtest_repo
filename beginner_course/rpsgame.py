import random
import json
import os

rolls = {"Nothing": "Here"}


def main():
    load_rolls()
    show_header()
    play_game("You", "Computer")


def show_header():
    print()
    print("---------------------------------")
    print("      Rock, Paper, Scissors")
    print("            version 2")
    print("     Data Structures Edition")
    print("---------------------------------")
    print()


def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}

    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Try again.")
            continue

        print(f"{player_1} roll {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round is a tie.")
        else:
            print(f"{winner} take(s) the round.")
            wins[winner] += 1

        print(f"Current score is {wins}")
        print()

    overall_winner = find_winner(wins, wins.keys())

    print(f"{overall_winner} win(s) the game.")
    print()


def get_roll(player_name, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, please choose roll? [rock, paper, scissors]: ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(roll_names):
        print(f"Sorry {player_name}, {text} is not a valid play.")
        return None

    return roll_names[selected_index]


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_winning_throw(player_1, player_2, roll1, roll2):

    if roll1 == roll2:
        print("The play was tied.")

    outcome = rolls.get(roll1, {})

    if roll2 in outcome.get("defeats"):
        return player_1
    elif roll2 in outcome.get("defeated_by"):
        return player_2


def load_rolls():
    global rolls
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rolls.json')

    with open(filename, 'r', encoding='utf-8') as fin:
        rolls = json.load(fin)

    print(f"Loaded rolls: {list(rolls.keys())}")


if __name__ == "__main__":
    main()
