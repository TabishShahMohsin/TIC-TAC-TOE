import random
import os
from collections import defaultdict

'''
import os

def print_big_grid(l, n):
    """Prints the Tic-Tac-Toe grid with big symbols and corner numbers."""
    os.system("cls" if os.name == "nt" else "clear")
    # ASCII representations of X and O
    X = [
        "  \\   /  ",
        "   \\ /   ",
        "    X    ",
        "   / \\   ",
        "  /   \\  "
    ]
    O = [
        "   ***   ",
        "  *   *  ",
        "  *   *  ",
        "  *   *  ",
        "   ***   "
    ]
    EMPTY = [
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]

    cell_size = 5
    grid = []

    for i in range(n):
        for row in range(cell_size):  # Rows for each ASCII representation
            line = ""
            for j in range(n):
                idx = i * n + j + 1
                symbol = l[idx - 1]
                if symbol == "x":
                    cell = X[row]
                elif symbol == "o":
                    cell = O[row]
                else:
                    cell = EMPTY[row]

                if row == 0:  # Top-left corner number
                    cell = f"({idx})" + cell[4:]
                line += cell + " | "
            grid.append(line.strip("| "))
        if i != n - 1:  # Add row separator
            grid.append("-" * (n * (cell_size + 3)))

    for line in grid:
        print(line)

def main():
    n = 3  # Size of the grid
    l = [" "] * (n * n)  # Empty grid
    print_big_grid(l, n)

    # Demonstration of gameplay loop
    for turn in range(1, n * n + 1):
        player = "x" if turn % 2 != 0 else "o"
        move = int(input(f"Player {player.upper()}, choose a cell (1-{n*n}): ")) - 1
        if l[move] == " ":
            l[move] = player
        else:
            print("Cell already occupied! Try again.")
            continue

        print_big_grid(l, n)

        # Add your win-check logic here (e.g., check_who_won)
        # Break loop if someone wins

    print("Game over!")

if __name__ == "__main__":
    main()
'''

HIGHSCORE_FILE = "highscores.txt"

def print_grid(l, n):
    """Print the game grid with a visually enhanced format."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(n):
        print("|", end="")
        for j in range(n):
            symbol = l[i * n + j]
            colored = f"\033[91m{symbol}\033[0m" if symbol == "x" else (
                f"\033[94m{symbol}\033[0m" if symbol == "o" else f"{symbol}")
            print(f" {colored} ", end="|")
        print()
        if i != n - 1:
            print(" ---" * n)

def check_who_won(l, n):
    """Determine if a player has won or if it's a draw."""
    for i in range(n):
        # Rows
        if l[i * n:i * n + n].count(l[i * n]) == n and l[i * n] != " ":
            return 1 if l[i * n] == "x" else -1
        # Columns
        if [l[j] for j in range(i, n * n, n)].count(l[i]) == n and l[i] != " ":
            return 1 if l[i] == "x" else -1

    # Diagonals
    if [l[i * (n + 1)] for i in range(n)].count(l[0]) == n and l[0] != " ":
        return 1 if l[0] == "x" else -1
    if [l[(i + 1) * (n - 1)] for i in range(n)].count(l[n - 1]) == n and l[n - 1] != " ":
        return 1 if l[n - 1] == "x" else -1

    # Draw
    if " " not in l:
        return 0
    return 2

def minimax(l, n, is_maximizing, memo):
    """Optimized minimax with memoization for better performance."""
    state = tuple(l)
    if state in memo:
        return memo[state]

    result = check_who_won(l, n)
    if result != 2:
        return result

    scores = []
    for i in range(n * n):
        if l[i] == " ":
            l[i] = "x" if is_maximizing else "o"
            score = minimax(l, n, not is_maximizing, memo)
            scores.append(score)
            l[i] = " "

    memo[state] = max(scores) if is_maximizing else min(scores)
    return memo[state]

def computer_move(l, n, difficulty):
    """Choose the computer's move based on the difficulty level."""
    if difficulty == "easy":
        # Random move
        move = random.choice([i for i, x in enumerate(l) if x == " "])
    elif difficulty == "medium":
        # Minimax with 50% randomization
        if random.random() < 0.5:
            move = random.choice([i for i, x in enumerate(l) if x == " "])
        else:
            move = best_move(l, n)
    else:  # Hard
        move = best_move(l, n)
    l[move] = "x"

def best_move(l, n):
    """Calculate the best move using minimax."""
    best_score = float("-inf")
    move = -1
    for i in range(n * n):
        if l[i] == " ":
            l[i] = "x"
            score = minimax(l, n, False, {})
            l[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def update_highscores(name, score):
    """Update the high score file with the player's score."""
    scores = []

    try:
        with open(HIGHSCORE_FILE, "r") as file:
            scores = [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        pass

    scores.append((name, score))
    scores.sort(key=lambda x: int(x[1]), reverse=True)

    with open(HIGHSCORE_FILE, "w") as file:
        for name, score in scores:
            file.write(f"{name},{score}\n")

def load_highscores():
    """Load high scores from the file."""
    try:
        with open(HIGHSCORE_FILE, "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        return []

def main():
    n = int(input("Enter grid size (n): "))
    print_grid([str(i + 1) for i in range(n * n)], n)

    choice = input("\nWelcome to TicTacToe! Would you like to play as X or O? ").lower()
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

    l = [" "] * (n * n)
    stats = defaultdict(int)

    while True:
        if choice == "o":
            computer_move(l, n, difficulty)
            print_grid(l, n)
            result = check_who_won(l, n)
            if result != 2:
                break

        while True:
            try:
                move = int(input("Enter your move (1 to n*n): ")) - 1
                if l[move] == " ":
                    l[move] = choice
                    break
            except (ValueError, IndexError):
                print("Invalid move. Try again.")

        print_grid(l, n)
        result = check_who_won(l, n)
        if result != 2:
            break

        if choice == "x":
            computer_move(l, n, difficulty)
            print_grid(l, n)
            result = check_who_won(l, n)
            if result != 2:
                break

    if result == 1:
        print("X has won!")
        stats["x"] += 1
    elif result == -1:
        print("O has won!")
        stats["o"] += 1
    elif result == 0:
        print("It's a draw!")
        stats["draw"] += 1

    name = input("Enter your name for high scores: ")
    update_highscores(name, stats[choice])
    print("\nHighscores:")
    for score_name, score_value in load_highscores():
        print(f"{score_name}: {score_value}")

if __name__ == "__main__":
    main()