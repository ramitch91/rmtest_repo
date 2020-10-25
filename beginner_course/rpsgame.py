import datetime
import random
import json
import os

rolls = {}


def main():
    log("Game started")
    load_rolls()
    show_header()
    show_leaderboard()
    player1, player2 = get_players()
    play_game(player1, player2)
    log("Game Over")


def show_header():
    print()
    print("---------------------------------")
    print("      Rock, Paper, Scissors")
    print("            version 3")
    print("   Leaderboard & Rolls Edition")
    print("---------------------------------")
    print()


def show_leaderboard():
    leaders = load_leaders()
    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)
    print("LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins} -- {name}")
    print()
    print("--------------------------")
    print()


def get_players():
    p1 = input("Player 1, what is your name? ").capitalize()
    log(f"Player = {p1}")
    p2 = "Computer"
    return p1, p2


def play_game(player_1, player_2):
    log(f"New game starting between {player_1} and {player_2}")
    wins = {player_1: 0, player_2: 0}

    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Try again.")
            continue

        log(f"Round: {player_1} rolls {roll1} and {player_2} rolls {roll2}")
        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            msg = "This round is a tie."
            log(msg)
            print(msg)
        else:
            msg = f"{winner} take(s) the round."
            log(msg)
            print(msg)
            wins[winner] += 1

        msg = f"Current score is {wins}"
        log(msg)
        print(msg)
        print()

    overall_winner = find_winner(wins, wins.keys())

    msg = f"{overall_winner} win(s) the game."
    log(msg)
    print(msg)
    print()
    record_win(overall_winner)


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
    filename = os.path.join(directory, 'rpsrolls.json')

    with open(filename, 'r', encoding='utf-8') as fin:
        rolls = json.load(fin)

    log(f"Loaded rolls: {list(rolls.keys())}")


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "rpsleaderboard.json")

    with open(filename, 'w', encoding="utf-8") as fout:
        json.dump(leaders, fout)

    log("Winner recorded.")


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "rpsleaderboard.json")

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding="utf-8") as fin:
        return json.load(fin)


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rps.log')
    time_text = datetime.datetime.now().strftime('%c')

    with open(filename, 'a', encoding="utf-8") as fout:
        fout.write(f"{time_text}: ")
        fout.write(msg)
        fout.write("\n")


if __name__ == "__main__":
    main()
