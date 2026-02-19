# INPUT #
'''

'''
# PROCESS #
'''
get random number
use number to select category
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
    puzzles = [
        ("Albums", "The College Dropout"),
        ("Albums", "Late Registration"),
        ("Albums", "Graduation"),
        ("Albums", "My Beautiful Dark Twisted Fantasy"),
        ("Albums", "Yeezus"),
        ("Albums", "Watch the Throne"),
        ("Albums", "The Life of Pablo"),
        ("Albums", "ye"),
        ("Albums", "Kids See Ghosts"),
        ("Albums", "Jesus is King"),
        ("Albums", "Donda"),
        ("Albums", "Vultures"),
        ("Albums", "Bully"),
        ("Action Movie", 'Mad Max: Fury Road'),
        ("Action Movie", 'Die Hard'),
        ("Action Movie", 'John Wick'),
        ("Action Movie", 'Enter the Dragon')
        ]
    return random.choice(puzzles)

def displayPuzzle(name):



def showGuesses():
    

def showBoard(guesses, phrase):
    board = ""

    for letter in phrase:
        if letter.lower() in guesses or not letter.isalpha():
            board += letter
        else:
            board += "_"

    print("\n" + board)

def main():


if __name__ == "__main__":
    main()