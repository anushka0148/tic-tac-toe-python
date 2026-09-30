from board import show_board, board_is_full
from input_handler import get_move
from rules import check_winner


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def play_game(scores):
    board = create_board()
    player = "X"

    print("\nNew Round!")
    print("Positions on the board:")
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
            print(f"Player {player} wins!")
            scores[player] += 1
            return

        if board_is_full(board):
            show_board(board)
            print("It's a draw!")
            scores["Draws"] += 1
            return

        player = "O" if player == "X" else "X"
