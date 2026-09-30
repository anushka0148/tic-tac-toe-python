def check_winner(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    if all(board[i][i] == mark for i in range(3)):
        return True

    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False
