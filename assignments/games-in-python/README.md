
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game that reinforces string manipulation, loops, and conditional logic. Students will implement game flow, input validation, and user feedback.

## 📝 Tasks

### 🛠️	Core Hangman Game

#### Description
Create a playable Hangman game in Python that selects a secret word and lets the player guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list in the program.
- Prompt the player for single-letter guesses (case-insensitive) and ignore repeated guesses.
- Show current progress each turn using underscores and revealed letters (e.g., "_ a _ _ m a n").
- Track and display remaining incorrect attempts (e.g., "Attempts left: 5").
- Maintain and display a list of letters already guessed.
- End the game with a clear win or lose message and reveal the secret word if the player loses.
- Validate input (accept only single alphabetic characters) and provide friendly feedback on invalid input.

Example session:
```
Welcome to Hangman!
_ _ _ _ _ _
Guess a letter: a
Progress: _ a _ _ _ _
Guessed: a
Attempts left: 6

Guess a letter: e
Progress: _ a _ _ _ _
Guessed: a, e
Attempts left: 5
...
```

### 🛠️	Optional Enhancements

#### Description
Add one or more optional features to improve the game experience or code quality.

#### Requirements
Completed enhancement examples (pick any):

- Load words from an external file (`words.txt`) and handle file errors gracefully.
- Implement difficulty levels that change allowed attempts or word selection.
- Provide a hint system that reveals a random unrevealed letter (limited uses).
- Display simple ASCII-art hangman stages as attempts are lost.
- Write unit tests for core functions (e.g., `reveal_progress`, `apply_guess`, `is_game_over`).

## 📎 Starter code

Place your main script in `starter-code.py` and keep helper modules in the same folder where appropriate.

## ✅ Submission

Include:

- `starter-code.py` — the playable game.
- Optional: `words.txt` (if using file-based word lists) and tests (e.g., `tests/test_game.py`).

Good luck and have fun!
