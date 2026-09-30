def get_move(board, player):
    while True:
        choice = input(f"Player {player}, choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice)
        if position < 1 or position > 9:
            print("Position must be between 1 and 9.")
            continue

        row = (position - 1) // 3
        col = (position - 1) % 3

        if board[row][col] != " ":
            print("That position is already occupied. Choose another one.")
            continue

        return row, col
