#!/usr/bin/env python3
"""
magic_8_ball_v2.py
This program uses a random number generator to simulate a
Magic 8 Ball.
"""

import random

def main():
    print("The Magic 8 Ball knows all!")
    question = input("Ask a Yes/No question ([Enter] to stop): ")
    while question != "":
        randint = random.randrange(6)   # gets 0-3 randomly
        if randint == 0:
            print("Reply hazy. Try again.")
        elif randint == 1:
            print("Future uncertain. Ask again later.")
        elif randint == 2:
            print("It is decidedly so.")
        elif randint == 3:
            print("Absolutely!")
        elif randint == 4:
            print("No.")
        else:
            print("I'm afraid not!")
        question = input("Ask a Yes/No question ([Enter] to stop): ")
    
    print("Good luck!")


main()
