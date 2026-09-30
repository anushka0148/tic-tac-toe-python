def create_scores():
    return {"X": 0, "O": 0, "Draws": 0}


def show_scores(scores):
    print("\nScoreboard")
    print(f"Player X: {scores['X']}")
    print(f"Player O: {scores['O']}")
    print(f"Draws: {scores['Draws']}")
