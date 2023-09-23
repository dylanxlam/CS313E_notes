# File: WordGame.py
# Description: Given a dictionary and previous guesses, filter out the possible words.
# Student Name: Dylan Lam
# Student UT EID: DXL85
# Course Name: CS 313E
# Unique Number: 52605


import sys
from typing import List, Tuple

def wordgame(guesses: List[List[Tuple[str, str]]], dictionary: List[str]) -> List[str]:
    words = dictionary.copy()

    for guess in guesses:
        for i, (letter, color) in enumerate(guess):
            if color == 'G':
                words = [word for word in words if word[i] == letter]

            elif color == 'Y':
                words = [word for word in words if letter in word and word[i] != letter]

            elif color == 'B':
                words = [word for word in words if letter not in word]

    return words


def main():
    # Helper functions for reading in input.
    LINES = sys.stdin.read().splitlines()[::-1]
    def input(): return LINES.pop()
    mul = lambda: map(int, input().strip().split())
    strng = lambda: input().strip()

    # First two numbers correspond to the number of words in the dictionary
    # and the number of guesses, respectively.
    num_dictionary, num_guesses = mul()
    dictionary = [strng().upper() for _ in range(num_dictionary)]
    guesses = []

    # Following lines contain the word guessed and the colors.
    for _ in range(num_guesses):
        # Advance reader (skip blank line).
        input()
        guess = strng()
        colors = strng()
        assert len(guess) == len(colors)
        guesses.append([(letter.upper(), color) for letter, color in zip(list(guess), list(colors))])

    # Call `wordgame` function.
    filtered = wordgame(guesses, dictionary)
    if len(filtered) == 0:
        print('No matches.')
    else:
        print(' '.join(filtered))

if __name__ == "__main__":
    main()
