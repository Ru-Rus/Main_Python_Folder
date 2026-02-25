# Rock Paper Scissors Ultimate (Tkinter Edition)

A desktop Rock Paper Scissors game built with Python and Tkinter.

This version includes:
- Best of 5 match system
- Multiple difficulty levels
- Adaptive AI that learns player patterns
- Persistent stats saved to file
- Clean GUI layout

---

## Features

### 1. Best of 5 Mode
- Game runs for 5 rounds.
- Final score is displayed in a popup.
- Stats are automatically saved after each completed match.

### 2. Difficulty Levels

- easy  
  Pure random computer moves.

- medium  
  50% random, 50% counter to player move.

- hard  
  Always counters the player's current move.

- adaptive  
  Tracks player history and counters the most frequently used move.

### 3. Adaptive AI Logic

The AI:
- Stores player move history.
- Uses collections.Counter to detect most common move.
- Counters that move to increase win probability.

### 4. Score Tracking

Tracks:
- Wins
- Losses
- Draws
- Current round

Displays live scoreboard in the UI.

### 5. Persistent Stats

After each Best of 5 match:

A file named:

stats.txt

Is updated with:

Wins:X, Losses:Y, Draws:Z

Each match appends a new line.

---

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with standard Python)

No external packages required.

---

## How to Run

1. Save the script as:

Rock_Paper_Scissors_Ultimate.py.py

2. Open terminal in the project folder.

3. Run:

python Rock_Paper_Scissors_Ultimate.py.py

The game window will open.

---

## Project Structure

Rock_Paper_Scissors_Ultimate.py.py  
stats.txt (auto-generated after first completed match)

---

## Core Game Flow

1. Player selects Rock, Paper, or Scissors.
2. AI selects move based on difficulty.
3. Winner is determined.
4. Scoreboard updates.
5. After 5 rounds:
   - Results popup appears
   - Stats saved to file

---

## Main Functions Overview

counter_move(move)  
Returns the winning counter for a given move.

adaptive_ai()  
Analyzes player history and counters most used move.

get_computer_choice(player_choice)  
Returns AI move based on difficulty.

determine_winner(player, computer)  
Returns "win", "lose", or "draw".

save_stats()  
Appends match results to stats.txt.

play(choice)  
Handles one round of gameplay.

reset_game()  
Resets scores and state for a new match.

---

## Possible Improvements

- Dark theme UI
- Sound effects
- SQLite database instead of text file
- Player name system
- Leaderboard
- Match history viewer
- Animations

---

## Author

Built as part of a Python desktop GUI project.
Designed to demonstrate:
- Tkinter GUI handling
- Game state management
- Basic AI logic
- File persistence
- Structured function design

---

Enjoy the game.