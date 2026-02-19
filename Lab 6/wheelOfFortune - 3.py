# INPUT #
'''

'''
# PROCESS #
'''
get random number
use number to select categoruy
get guess
check if in phrase
if in phrase place letter in a set of underscores

'''
# OUTPUT #
'''
Welcome to Wheel of Fortune!
You have to guess the phrase before you make 7 wrong guesses
Good luck

Your pusszle is from the category: category (ex Action Movie)

_________ ______ ________

what letter would you like?
R
You have guessed: ['r']

____r ___ _r____
'''

import random

def getPuzzle():

def displayPuzzle(name):
    """This function returns a tuple (Category, Phrase) that can be used to play a simple game of like Wheel of Fortune."""
    puzzles = [("Famous People", "Abraham Lincoln"), ("Famous People", "Oprah Winfrey"), ("Famous People", "Will Smith"), ("Famous People", "Marilyn Monroe"), ("Action Movie", 'Mad Max: Fury Road'),  ("Action Movie", 'Die Hard'),  ("Action Movie", 'John Wick'),  ("Action Movie", 'Enter the Dragon')]
    index = random.randint(0, len(puzzles)-1)
    return puzzles[index]


def showGuesses():


def showBoard(guesses, name):


def main():


if __name__ == "__main__":
    main()