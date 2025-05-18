# Tic-Tac-Toe AI (with Pygame + Minimax)

This is a Python-based Tic-Tac-Toe game where you play against an intelligent AI opponent. The AI uses the **Minimax algorithm** to make optimal moves every time. The game features a clean and simple **Pygame** interface.

## Features

- Play as **X** or **O**
- AI opponent that **never loses**
- Built using **Pygame** for visuals
- Implements the **Minimax algorithm** with alpha pruning for efficiency
- Option to **restart** the game after every match

## Files

- `runner.py` — Main file to run the GUI and handle game logic with Pygame
- `tictactoe.py` — Core Tic-Tac-Toe engine including game rules and Minimax implementation
- `OpenSans-Regular.ttf` — Font file used for UI rendering

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Run the runner.py to play the game!

## AI Logic

- **Minimax Algorithm**: Recursively simulates every possible outcome and chooses the move that minimizes the possible loss.
- **Optimal Play**: The AI will always either win or draw — never lose.

## Inspiration

This project was inspired by Harvard's CS50 AI course — implemented with some personal enhancements and UI styling using Pygame.

---
