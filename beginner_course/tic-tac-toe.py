import random
import os
import datetime
import json
from colorama import Fore


# x - create the board
# x - choose the players
# x - choose an initial player
# until someone wins (Check for a winner)
#   x - show the board
#   Choose a location, check to see if it is already  marked, mark it
#   toggle active player
# game over (active player won)


def main():
    print(Fore.WHITE)
    log("Start Game...")
    show_header
    show_leaderboard()
    # CREATE THE BOARD
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    # CHOOSE INITIAL PLAYER
    active_player_index = 0
    player_name = input("Enter your name: ")
    log(f"Player = {player_name.capitalize()}")
    players = [player_name.capitalize(), "Computer"]
    symbols = ["X", "O"]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)

        # CHOOSE LOCATION
        if not choose_location(board, symbol, players[active_player_index]):
            print(Fore.RED + "That isn't an option, try again." + Fore.WHITE)
            continue

        # TOGGLE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    fore = Fore.GREEN if player == players[0] else Fore.RED
    print(fore)
    print("-----------------------------")
    print()
    print(fore + f"Game Over! {player} has won with the board: " + Fore.WHITE)
    print()
    show_board(board)
    print(fore + "-----------------------------")
    print(Fore.WHITE)
    log(f"Game Over! {player} won")
    record_win(player)


# Board is a list of rows
# Rows are a list of cells


def show_header():
    print(Fore.MAGENTA)
    print("-----------------------------------")
    print("        Tic-Tac-Toe Game")
    print("           version 2")
    print("-----------------------------------")
    print(Fore.WHITE)


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()


def show_board(board):
    for row in board:
        print("| ", end="")
        for cell in row:
            symbol = cell if cell is not None else "-"
            if symbol == "X":
                fore = Fore.GREEN
            elif symbol == "O":
                fore = Fore.YELLOW
            else:
                fore = Fore.WHITE
            print(fore + symbol + Fore.WHITE, end=" | ")
        print()
    print()


def choose_location(board, symbol, player):
    if player == "Computer":
        row = random.randint(1, 3)
        column = random.randint(1, 3)
    else:
        try:
            row = int(input("Choose which row: "))
        except ValueError:
            print(Fore.RED + "You must enter a number from 1  to 3" + Fore.WHITE)
            return False
        try:
            column = int(input("Choose which column: "))
        except ValueError:
            print(Fore.RED + "You must enter a number from 1  to 3" + Fore.WHITE)
            return False

    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # win by rows
    rows = board
    sequences.extend(rows)

    # win by columns
    for col_idx in range(0, 3):
        col = [board[0][col_idx], board[1][col_idx], board[2][col_idx]]
        sequences.append(col)

    # win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "tictactoe.log")
    time_text = datetime.datetime.now().strftime("%c")

    with open(filename, "a", encoding="utf-8") as fout:
        fout.write(f"{time_text}: ")
        fout.write(msg)
        fout.write("\n")


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "3Tleaderboard.json")

    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


def show_leaderboard():
    leaders = load_leaders()
    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)
    print(Fore.CYAN + "LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins} -- {name}")
    print()
    print("--------------------------")
    print(Fore.WHITE)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "3Tleaderboard.json")

    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(leaders, fout)

    log("Winner recorded.")


if __name__ == "__main__":
    main()
