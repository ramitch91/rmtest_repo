import random

# x - create the board
# x - choose the players
# x - choose an initial player
# until someone wins (Check for a winner)
#   x - show the board
#   Choose a location, check to see if it is already  marked, mark it
#   toggle active player
# game over (active player won)


def main():
    show_header()
    # CREATE THE BOARD
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    # CHOOSE INITIAL PLAYER
    active_player_index = 0
    players = ["Ricky", "Computer"]
    symbols = ["X", "O"]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)

        # CHOOSE LOCATION
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print("-----------------------------")
    print()
    print(f"Game Over! {player} has won with the board: ")
    print()
    show_board(board)
    print("-----------------------------")
    print()


# Board is a list of rows
# Rows are a list of cells


def show_header():
    print()
    print("-----------------------------------")
    print("        Tic-Tac-Toe Game")
    print("           version 2")
    print("-----------------------------------")
    print()


def announce_turn(player):
    print()
    print(f"It's  {player}'s turn. Here's the board:")
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
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))

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
    columns = []
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


if __name__ == "__main__":
    main()