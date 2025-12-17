# Hangman Word Guess Game (Python)

A simple and fun **console-based Word Guessing game** built using Python. The player has to guess a randomly selected word by entering letters one at a time before running out of lives.

---

## Features

- Random word selection from a large word list
- Lives based on word length
- Letter-by-letter guessing
- Real-time display of guessed letters
- Win/Loss detection
- Beginner-friendly Python logic

---

## Tech Stack

- **Language:** Python 3
- **Library Used:** `random`
- **Platform:** Terminal / Command Prompt

---

## How the Game Works

1. A random word is selected from a predefined list
2. The number of lives equals the length of the word
3. The word is displayed as underscores (`_`)
4. The user guesses one letter at a time
5. Correct guesses reveal the letter positions
6. Wrong guesses reduce lives
7. Guess all letters before lives end to win

---

## How to Run the Game

### Step 1: Clone the Repository
```bash
git clone https://github.com/shivam183-star/Hangman-Word-Game.git
```

### Step 2: Navigate to Project Folder
```bash
cd Hangman-Word-Game
```

### Step 3: Run the Game
```bash
python main.py
```

> Make sure Python 3 is installed on your system

---

## Project Structure

```
word-guess-game/
│
├── main.py         # Main game file
├── README.md       # Project documentation
```

---

## Code Explanation

### Key Variables

- `words` → List of possible words
- `word` → Randomly selected word
- `lives` → Attempts allowed (equal to word length)
- `result` → Stores guessed letters

### Core Logic

- Uses `random.choice()` to select a word
- Uses a loop to keep the game running until win/loss
- Uses `enumerate()` to find all occurrences of a guessed letter

---

## Sample Gameplay

```
Guess letters of the word
_ _ _ _ _
5 lives left
Enter letter: a
_ a _ a _
```

---

## Future Improvements

- Avoid repeated letter guesses
- Difficulty levels (Easy / Medium / Hard)
- Add hint system
- GUI version using Tkinter or Pygame
- Score tracking

---

## Author

- **Shivam Singh**
- Student | Python Learner
- @Shivam183-star

---

## Support

If you like this project, please star the repository and share it!

Happy Coding & Enjoy Hangman!

