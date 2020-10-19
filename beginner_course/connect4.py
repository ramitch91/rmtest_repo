# Connect 4 Game
# steps needed
#   create the board
#   set up players and symbols
#   choose inital player
#   show board (6 rows by 7 columns)
#   make sure player chooses a valid play
#   check for winner
#       check for win horizontaly
#       check for win verticaly
#       check for win diagonally
#   choose location
#   rotate players
#   announce winner
#   show winning board


from typing import Sequence


def main():
    show_header()

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
    players = ["Ricky", "Computer"]
    symbols = ["R", "Y"]

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)

        if not choose_location(board, symbol):
            print("That is not a valid option. Please try again.")
            continue

        active_player_index = (active_player_index + 1) % len(players)


def show_header():
    print()
    print("--------------------------------------")
    print("           Connect 4 Game")
    print("             Version 1")
    print("--------------------------------------")
    print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here is the current board:")
    print()


def show_board(board):
    for row in board:
        print("| ", end="")
        for cell in row:
            symbol = cell if cell is not None else "-"
            print(symbol, end=" | ")
        print()
    print()


def choose_location(board, symbol):
    #    try:
    row = int(input("Choose a row: "))
    #    except:
    #        return False
    #    try:
    column = int(input("Choose a column: "))
    #    except:
    #        return False

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

    # Win by Rows
    rows = board
    sequences.extend(rows)

    # Win by Columns
    column = []
    for col_idx in range(0, 7):
        column = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
            board[3][col_idx],
            board[4][col_idx],
            board[5][col_idx],
        ]
        sequences.append(column)

    # Win by Diagonals
    diagonals = [
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

    sequences.extend(diagonals)

    return sequences


if __name__ == "__main__":
    main()