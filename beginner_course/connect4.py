# Connect 4 Game
# steps needed
#   create the board
#   set up players and symbols
#   choose initial player
#   show board (6 rows by 7 columns)
#   make sure player chooses a valid play
#   check for winner
#       check for win horizontally
#       check for win vertically
#       check for win diagonally
#   choose location
#   rotate players
#   announce winner
#   show winning board

import random
import datetime
import os
import json
from typing import List, Optional
from colorama import Fore


def main():
    log("Starting Game...")
    show_header()
    show_leaderboard()

    # CREATE THE BOARD
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # SETUP PLAYERS AND SYMBOLS
    active_player_index = 0
    player_name = input("Enter your name: ")
    players = [player_name.capitalize(), "Computer"]
    log(f"Player = {players[0]}")

    date_range = datetime.datetime.now().month
    if date_range == 1:
        symbols = ["❄", "🎿"]
    elif date_range == 2:
        symbols = ["💝", "💌"]
    elif date_range in (4, 5):
        symbols = ["🌼", "🌧️"]
    elif date_range == 7:
        symbols = ["🇺🇸", "🎆"]
    elif date_range == 10:
        symbols = ["🎃", "👻"]
    elif date_range == 11:
        symbols = ["🦃", "🥧"]
    elif date_range == 12:
        symbols = ["🎅", "🎄"]
    else:
        symbols = ["🍩", "🍦"]

    print(f"Welcome {players[0]}")
    print(f"Your symbol will be {symbols[0]}")
    print(f"{players[1]} will be {symbols[1]}")
    print()
    log(f"{players[0]} will be {symbols[0]} and {players[1]} will be {symbols[1]}.")

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)

        if not choose_location(board, symbol, player):
            print("That is not a valid option. Please try again.")
            continue

        active_player_index = (active_player_index + 1) % len(players)

    fore = Fore.GREEN if player == players[0] else Fore.RED
    print()
    print(fore + f"GAME OVER! {player} ({symbol}) has won with the board:" + fore)
    print()
    log(f"Game over! {player} ({symbol}) wins the game")
    show_board(board)
    print()

    record_win(player)


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


def show_header():
    print(Fore.MAGENTA)
    print("--------------------------------------")
    print("           Connect 4 Game")
    print("      External Library Edition")
    print("--------------------------------------")
    print(Fore.WHITE)


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here is the current board:")
    print()


def show_board(board):
    for row_idx, row in enumerate(board, start=1):
        print("| ", end="")
        for col_idx, cell in enumerate(row, start=1):
            empty_text = f"({row_idx}, {col_idx})"
            symbol = f"  {cell}  " if cell is not None else empty_text
            print(symbol, end=" | ")
        print()
    print()


def choose_location(board, symbol, player):
    if player == "Computer":
        column = random.randint(1, len(board[0]))
        print(f"Computer chooses column {column}")
    else:
        try:
            column = int(input("Choose a column: "))
        except TypeError:
            print("Oops! That was not a valid number.")
            return False

    column -= 1
    if column < 0 or column >= len(board[0]):
        return False

    row = find_bottom_row(board, column)
    if row is None:
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def find_bottom_row(board: List[List[str]], column: int) -> Optional[int]:
    col_cells = [board[n][column] for n in range(0, len(board))]
    last_empty = None
    for idx, cell in enumerate(col_cells):
        if cell is None:
            last_empty = idx
    return last_empty


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # Win by Rows
    rows = board
    # Go through each row and get any consecutive sequence of four cells in a row
    for row in rows:
        four_across = find_sequences_of_four_cells_in_a_row(row)
        sequences.extend(four_across)

    # Win by Columns
    for col_idx in range(0, 7):
        column = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
            board[3][col_idx],
            board[4][col_idx],
            board[5][col_idx],
        ]
        # Go through each column and get any consecutive sequence of four cells in a row
        four_down = find_sequences_of_four_cells_in_a_row(column)
        sequences.extend(four_down)

    # Win by Diagonals
    diagonals = [
        # test for diagonals up and to the right
        # [board[0][0]],
        # [board[1][0], board[0][1]],
        # [board[2][0], board[1][1], board[0][2]],
        [board[3][0], board[2][1], board[1][2], board[0][3]],
        [board[4][0], board[3][1], board[2][2], board[1][3], board[0][4]],
        [board[5][0], board[4][1], board[3][2], board[2][3], board[1][4], board[0][5]],
        [board[5][1], board[4][2], board[3][3], board[2][4], board[1][5], board[0][6]],
        [board[5][2], board[4][3], board[3][4], board[2][5], board[1][6]],
        [board[5][3], board[4][4], board[3][5], board[2][6]],
        # [board[5][4], board[3][5], board[2][6]],
        # [board[5][5], board[4][6]],
        # [board[5][6]],
        # test for diagonals down and to the right
        # [board[0][6]],
        # [board[0][5], board[1][6]],
        # [board[0][4], board[1][5], board[2][6]],
        [board[0][3], board[1][4], board[2][5], board[3][6]],
        [board[0][2], board[1][3], board[2][4], board[3][5], board[4][6]],
        [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5], board[5][6]],
        [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]],
        [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]],
        [board[2][0], board[3][1], board[4][2], board[5][3]],
        # [board[3][0], board[4][1], board[5][2]],
        # [board[4][0], board[5][1]],
        # [board[5][0]]
    ]
    # Go through the diagonals to see if there are four consecutive cells in a row
    for diag in diagonals:
        four_diagonal = find_sequences_of_four_cells_in_a_row(diag)
        sequences.extend(four_diagonal)

    return sequences


def find_sequences_of_four_cells_in_a_row(cells: List[str]) -> List[List[str]]:
    sequences = []
    for n in range(0, len(cells) - 3):
        candidate = cells[n : n + 4]
        if len(candidate) == 4:
            sequences.append(candidate)
    return sequences


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "c4leaderboard.json")

    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "c4leaderboard.json")

    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(leaders, fout)

    log("Winner recorded")


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, "c4.log")
    time_text = datetime.datetime.now().strftime("%c")

    with open(filename, "a", encoding="utf-8") as fout:
        fout.write(f"{time_text}: ")
        fout.write(msg)
        fout.write("\n")


if __name__ == "__main__":
    main()
