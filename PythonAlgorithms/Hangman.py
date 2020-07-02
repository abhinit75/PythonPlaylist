# The Game of Hangman


import random, sys
from typing import List

# TODO try to load these from a text file
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]

GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) # lets randomize single word from the list
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

# Utility functions

def print_word_to_guess(letters: List) -> None:
    """Utility function to print the current word to guess"""
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    """Prints how many chances the player has used"""
    print("You are on guess {0}/{1}.".format(current, total))


# Game functions

def beginning() -> None:
    """Starts the game"""
    print("Hello Mate!\n")
    while True:
        name = input("Please enter Your name\n").strip()
        if name == '':
            print("You can't do that! No blank lines")
        else:
            break


def ask_user_to_play() -> None:
    """Ask user if they want to play"""
    print("Well, that's perfect moment to play some Hangman!\n")
    while True:
        gameChoice = input("Would You?\n").upper()
        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue


def prepare_secret_word() -> None:
    """Prepare secret word and inform user of it"""
    for character in SECRET_WORD: # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    print("Ok, so the word You need to guess has", LENGTH_WORD, "characters")
    print("Be aware that You can enter only 1 letter from a-z\n\n")
    print_word_to_guess(GUESS_WORD)


def guessing() -> None:
    """
    Main game loop to have user guess letters
    and inform them of the results
    """
    guess_taken = 1
    MAX_GUESS = 10
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n").lower()
        if not guess in ALPHABET: #checking input
            print("Enter a letter from a-z ALPHABET")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("You won!")
                    print("Game Over!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was {0}".format(SECRET_WORD))


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()