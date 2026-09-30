from game import play_game
from scoreboard import create_scores, show_scores


def main():
    scores = create_scores()
    print("Welcome to Tic-Tac-Toe!")

    while True:
        play_game(scores)
        show_scores(scores)

        again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
