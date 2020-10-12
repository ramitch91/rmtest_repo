import random
from typing import NoReturn

rolls = {
    "rock": {"defeats": ["scissors"], "defeated_by": ["paper"]},
    "paper": {"defeats": ["rock"], "defeated_by": ["scissors"]},
    "scissors": {"defeats": ["paper"], "defeated_by": ["rock"]},
}


def main():
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
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    roll_names = list(rolls.keys())

    while wins_p1 < rounds and wins_p2 < rounds:
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
            if winner == player_1:
                print(f"{winner} take the round.")
                wins_p1 += 1
            elif winner == player_2:
                print(f"{winner} takes the round.")
                wins_p2 += 1

        print(f"Score is {player_1}: {wins_p1} and {player_2}: {wins_p2}.")
        print()

    if wins_p1 >= rounds:
        overall_winner = player_1
        winning_statement = "win the game"
    else:
        overall_winner = player_2
        winning_statement = "wins the game"

    print(f"{overall_winner} {winning_statement}.")
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


def check_winning_throw(player_1, player_2, roll1, roll2):

    if roll1 == roll2:
        print("The play was tied.")

    outcome = rolls.get(roll1, {})

    if roll2 in outcome.get("defeats"):
        return player_1
    elif roll2 in outcome.get("defeated_by"):
        return player_2


if __name__ == "__main__":
    main()
