# Tic-Tac-Toe with Scoreboard
# A simple two-player game using lists, loops, conditions and functions.

def show_board(board):
    """Display the current 3 by 3 board."""
    print()
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board, mark):
    """Return True if the given mark has a winning line."""
    # Check each row and each column.
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
        if all(board[j][i] == mark for j in range(3)):
            return True

    # Check the two diagonals.
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False


def board_is_full(board):
    """Return True when there are no empty cells left."""
    for row in board:
        if " " in row:
            return False
    return True


def get_move(board, player):
    """Ask the current player for a valid position from 1 to 9."""
    while True:
        choice = input(f"Player {player}, choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice)
        if position < 1 or position > 9:
            print("That position is outside the board. Try again.")
            continue

        # Convert the position number into row and column.
        row = (position - 1) // 3
        col = (position - 1) % 3

        if board[row][col] != " ":
            print("That position is already taken. Choose another.")
            continue

        return row, col


def play_game(scores):
    """Play one round and update the scoreboard."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("\nPositions on the board:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        show_board(board)
        row, col = get_move(board, player)
        board[row][col] = player

        if check_winner(board, player):
            show_board(board)
            print(f"Player {player} wins this round!")
            scores[player] += 1
            return

        if board_is_full(board):
            show_board(board)
            print("This round is a draw.")
            scores["Draws"] += 1
            return

        # Switch between X and O.
        player = "O" if player == "X" else "X"


def main():
    """Run rounds until the players choose to exit."""
    scores = {"X": 0, "O": 0, "Draws": 0}

    print("Welcome to Tic-Tac-Toe!")
    while True:
        play_game(scores)
        print("\nScoreboard")
        print(f"Player X: {scores['X']}")
        print(f"Player O: {scores['O']}")
        print(f"Draws: {scores['Draws']}")

        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
