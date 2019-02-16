#!/usr/bin/env python3
"""
number_guessing_game.py
This program makes up a secret (random) number between 1 and 10,
and gives the user 3 tries to guess it. If the user hasn't
guessed after three tries, then number is revaled.
"""

import random

def main():
    randint = random.randrange(10) + 1  # gets a number 1-10 inclusive
    guess = 0
    tries = 1
    print("I'm thinking of a number between 1 and 10.")
    print("You have three tries to guess it!")
    while tries < 4 and guess != randint:
        print("Your guess: ",end='')
        guess = eval(input())
        if guess == randint:
            print("You got it!")
        else:
            print("Darnit, that's not it!")
            if guess < randint:
                print("Guess higher!")
            else:
                print("Guess lower!")
        tries = tries + 1
    print("The number was",randint)

main()

