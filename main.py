# Hangman — Countries Edition 🌍

import random
import sys

WORDS = [
    "argentina","australia","austria","brazil","belgium","canada","chile","china",
    "colombia","croatia","cuba","czechia","denmark","egypt","estonia","finland",
    "france","germany","greece","hungary","iceland","india","indonesia","iran",
    "iraq","ireland","palestine","italy","japan","jordan","kenya","latvia","lebanon",
    "lithuania","luxembourg","malaysia","mexico","morocco","netherlands","newzealand",
    "nigeria","norway","pakistan","peru","philippines","poland","portugal","qatar",
    "romania","russia","saudiarabia","serbia","singapore","slovakia","slovenia",
    "southafrica","southkorea","spain","sweden","switzerland","syria","thailand",
    "tunisia","turkey","ukraine","unitedkingdom","unitedstates","uruguay","venezuela",
    "vietnam","yemen","zambia","zimbabwe"
]

HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
]

MAX_WRONG = len(HANGMAN_STAGES) - 1

def mask_word(secret, guessed):
    return " ".join([c.upper() if c in guessed else "_" for c in secret])

def display(secret, guessed, wrong):
    stage = HANGMAN_STAGES[wrong]
    print(stage)
    print(f"Word:   {mask_word(secret, guessed)}")
    print(f"Lives:  {MAX_WRONG - wrong} / {MAX_WRONG}")
    print("-" * 26)

def get_input(prompt="Your guess: "):
    while True:
        s = input(prompt).strip().lower()
        if not s:
            print("Please type a letter or word.")
            continue
        if s.isalpha():
            return s
        print("Letters only please.")

def play_one_round():
    secret = random.choice(WORDS).lower()
    guessed = set()
    wrong = 0

    print("\nI’ve picked a country. Good luck!\n")
    display(secret, guessed, wrong)

    while True:
        if wrong >= MAX_WRONG:
            print(f"💀 You lost! The country was {secret.upper()}.")
            break
        if all(c in guessed for c in secret):
            print(f"🎉 You win! The country was {secret.upper()}.")
            break

        guess = get_input()

        if len(guess) > 1:
            # Add letters from guess that appear in secret
            for c in guess:
                if c in secret:
                    guessed.add(c)
            if guess == secret:
                guessed.update(secret)
                display(secret, guessed, wrong)
                print(f"🎉 You win! The country was {secret.upper()}.")
                break
            else:
                wrong += 1
                print(f"❌ {guess.upper()} is not the country.")
        else:
            letter = guess
            if letter in guessed:
                print(f"↩️ Already tried {letter.upper()}.")
            elif letter in secret:
                guessed.add(letter)
                print(f"✅ {letter.upper()} is in the country!")
            else:
                wrong += 1
                print(f"❌ {letter.upper()} is not in the country.")

        display(secret, guessed, wrong)

def main():
    print("""
========================
    H A N G M A N 🌍
========================
Theme: Countries
Guess letters or whole names (no spaces).
Correct letters will appear in the word (_ _ _ _).
Lives lost only on wrong guesses.
""")
    while True:
        play_one_round()
        again = input("Play again? (y/n) ").strip().lower()
        if not again.startswith("y"):
            print("Thanks for playing Hangman! 👋")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
