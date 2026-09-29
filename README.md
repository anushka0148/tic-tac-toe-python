# tic-tac-toe-python
An interactive Tic-Tac-Toe game developed using Python, featuring game logic, player turns,and win detection.
# 🎮 Tic-Tac-Toe with Scoreboard

A simple two-player Tic-Tac-Toe game developed using Python. The game allows two players to play multiple rounds while keeping track of their scores.

## 📌 About the Project

This project is a console-based implementation of the classic **Tic-Tac-Toe** game.

Players **X** and **O** take turns choosing positions on a 3×3 board. The program checks for winning combinations, detects draws, validates player inputs, and maintains a scoreboard across multiple rounds.

## ✨ Features

* Two-player gameplay
* 3×3 game board
* Position selection from 1–9
* Win detection for rows, columns, and diagonals
* Draw detection
* Prevents already occupied positions
* Handles invalid inputs
* Scoreboard for multiple rounds
* Option to play another round

## 🛠️ Technologies Used

* **Python 3**
* Lists and nested lists
* Functions
* Loops
* Conditional statements
* User input and validation

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/anushka0148/tic-tac-toe-python.git
```

### 2. Open the project folder

```bash
cd tic-tac-toe-python
```

### 3. Run the game

```bash
python tic_tac_toe.py
```

## 🎯 How to Play

The board positions are numbered as:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

* Player **X** starts the game.
* Enter a number from **1 to 9** to select a position.
* Players take turns between X and O.
* The game checks for a winner after every move.
* If all positions are filled without a winner, the round is a draw.
* After each round, the scoreboard is displayed.
* Players can choose whether to play another round.

## 🧠 Main Functions

| Function          | Purpose                                                |
| ----------------- | ------------------------------------------------------ |
| `show_board()`    | Displays the current 3×3 board                         |
| `check_winner()`  | Checks rows, columns, and diagonals for a winning line |
| `board_is_full()` | Checks whether there are no empty positions            |
| `get_move()`      | Takes and validates the player's move                  |
| `play_game()`     | Controls one complete round                            |
| `main()`          | Runs the game and manages the scoreboard               |

The program uses separate functions for different parts of the game, making the code easier to understand and manage.

## 🔄 Basic Game Flow

```text
Start
  ↓
Display Board
  ↓
Player chooses a position
  ↓
Validate Input
  ↓
Place X / O
  ↓
Check Winner
  ↓
Winner?
 ├── Yes → Update Score → End Round
 │
 └── No
      ↓
   Board Full?
    ├── Yes → Draw → End Round
    │
    └── No
         ↓
     Switch Player
         ↓
    Continue Game
```

## 📚 Concepts Used

This project demonstrates basic Python programming concepts such as:

* Functions
* Lists and nested lists
* `for` loops
* `while` loops
* `if-else` conditions
* Input validation
* Boolean expressions
* String formatting
* Basic problem-solving and game logic

## 📷 Sample Output

```text
Welcome to Tic-Tac-Toe!

Positions on the board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player X, choose a position (1-9):
```

Author : Anushka

GitHub: **[@anushka0148](https://github.com/anushka0148)**


