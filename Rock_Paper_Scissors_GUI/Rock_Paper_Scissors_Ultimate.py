import random
import tkinter as tk
from tkinter import messagebox
from collections import Counter

# ===== GAME CONFIG =====
choices = ["Rock", "Paper", "Scissors"]
player_history = []
wins = 0
losses = 0
draws = 0
round_count = 0
difficulty = "easy"
MAX_ROUNDS = 5


# ===== AI SYSTEM =====
def counter_move(move):
    counters = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
    return counters[move]


def adaptive_ai():
    if not player_history:
        return random.choice(choices)
    most_common = Counter(player_history).most_common(1)[0][0]
    return counter_move(most_common)


def get_computer_choice(player_choice):
    if difficulty == "easy":
        return random.choice(choices)

    if difficulty == "medium":
        if random.random() < 0.5:
            return random.choice(choices)
        return counter_move(player_choice)

    if difficulty == "hard":
        return counter_move(player_choice)

    if difficulty == "adaptive":
        return adaptive_ai()


# ===== GAME LOGIC =====
def determine_winner(player, computer):
    if player == computer:
        return "draw"

    if (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "win"

    return "lose"


def save_stats():
    with open("stats.txt", "a") as f:
        f.write(f"Wins:{wins}, Losses:{losses}, Draws:{draws}\n")


def play(choice):
    global wins, losses, draws, round_count

    if round_count >= MAX_ROUNDS:
        return

    player_history.append(choice)
    computer = get_computer_choice(choice)

    result = determine_winner(choice, computer)

    if result == "win":
        wins += 1
        result_text.set(f"You WIN! Computer chose {computer}")
    elif result == "lose":
        losses += 1
        result_text.set(f"You LOSE! Computer chose {computer}")
    else:
        draws += 1
        result_text.set(f"DRAW! Computer chose {computer}")

    round_count += 1
    update_score()

    if round_count == MAX_ROUNDS:
        save_stats()
        messagebox.showinfo(
            "Game Over",
            f"Final Score\n\nWins: {wins}\nLosses: {losses}\nDraws: {draws}"
        )


def update_score():
    score_text.set(
        f"Round {round_count}/{MAX_ROUNDS}   |   Wins: {wins}   Losses: {losses}   Draws: {draws}"
    )


def reset_game():
    global wins, losses, draws, round_count, player_history
    wins = losses = draws = round_count = 0
    player_history = []
    result_text.set("Make your move")
    update_score()


def set_difficulty(d):
    global difficulty
    difficulty = d


# ===== UI SETUP =====
root = tk.Tk()
root.title("Rock Paper Scissors Ultimate")
root.geometry("500x400")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
title.pack(pady=15)

score_text = tk.StringVar()
score_label = tk.Label(root, textvariable=score_text, font=("Arial", 11))
score_label.pack()

result_text = tk.StringVar(value="Make your move")
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 13))
result_label.pack(pady=15)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for move in choices:
    tk.Button(
        button_frame,
        text=move,
        width=12,
        height=2,
        font=("Arial", 11),
        command=lambda m=move: play(m)
    ).pack(side="left", padx=10)

# Difficulty Section
diff_label = tk.Label(root, text="Difficulty", font=("Arial", 12, "bold"))
diff_label.pack(pady=10)

difficulty_var = tk.StringVar(value="easy")

for diff in ["easy", "medium", "hard", "adaptive"]:
    tk.Radiobutton(
        root,
        text=diff.capitalize(),
        variable=difficulty_var,
        value=diff,
        command=lambda d=diff: set_difficulty(d)
    ).pack()

reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 11),
    width=15,
    command=reset_game
)
reset_btn.pack(pady=15)

update_score()

root.mainloop()