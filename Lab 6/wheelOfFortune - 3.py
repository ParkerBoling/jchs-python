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
        # albums
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
        # songs
        ("Songs", 'All Falls Down'),
        ("Songs", 'We Major'),
        ("Songs", 'Diamonds From Sierra Leone'),
        ("Songs", "Can't Tell Me Nothing"),
        ("Songs", "On Sight"),
        ("Songs", "Runaway"),
        ("Songs", "All of the Lights"),
        ("Songs", "Hurricane"),
        ("Songs", "Life of the Party"),
        ("Songs", "Two Words"),
        ("Songs", "Welcome to Heartbreak"),
        # features
        ("Features", "Playboi Carti"),
        ("Features", "Jay-Z"),
        ("Features", "Travis Scott"),
        ("Features", "Kid Cudi"),
        ("Features", "Pusha T"),
        ("Features", "Nicki Minaj"),
        ("Features", "Rick Ross"),
        ("Features", "Common"),
        ("Features", "Consequence"),
        ("Features", "Andre Three-Thousand"),
        ("Features", "Kendrick Lamar")
        ("Features", "The Weeknd"),
        ]
    return random.choice(puzzles)

def displayPuzzle(category):
    print("Welcome to Wheel of Fortune! (ye edition)")
    print("You have to guess the phrase before you make 7 wrong guesses")
    print("Good luck!")
    print("\nYour puzzle is from the category:", category)

def showBoard(guesses, phrase):
    board = ""

    for letter in phrase:
        if letter.lower() in guesses or not letter.isalpha():
            board += letter
        else:
            board += "_"

    print("\n" + board)

def showGuesses(guesses):
    print("You have guessed:", guesses)


def main():
    category, phrase = getPuzzle()
    guesses = []
    wrongGuesses = 0
    maxWrong = 7

    displayPuzzle(category)

    while wrongGuesses < maxWrong:
        boardComplete = True
        showBoard(guesses, phrase)
        
        for letter in phrase:
            if letter.isalpha() and letter.lower() not in guesses:
                boardComplete = False
        
        if boardComplete:
            print("\nYou Win!")
            print("The phrase was:", phrase)
            return
        
        guess = input("\nWhat letter would you like? ").lower()
        
        # check if more than one letter
        if not guess.isalpha() or len(guess) != 1:
            print("Input invalid. Enter max one letter.")
            continue
        
        if guess in guesses:
            print("you already guessed that letter, try again.")
            continue
        
        guesses.append(guess)
        
        if guess not in phrase.lower():
            wrongGuesses += 1
            print("Wrong Guess!")
            print("You have", maxWrong - wrongGuesses, "wrong guesses left.")
        
        showGuesses(guesses)

    # if loop ends, lose
    print("\nYou lose")
    print("The phrase was:", phrase)
        

if __name__ == "__main__":
    main()