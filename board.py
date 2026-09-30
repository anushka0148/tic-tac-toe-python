def show_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")


def board_is_full(board):
    return all(cell != " " for row in board for cell in row)
