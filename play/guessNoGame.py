import random

def randomFig():
    figure = random.randint(1, 20)
    return figure

def welcome():
    print ("Welcome to guess the number game! Guess the number between 1 and 20! You have 7 guesses! Take a Guess:")

def events(figure):
    for guesstaken in range(1,7):
        guess = int(input())

        if figure > guess:
            print ("Wrong. The answer is higher")
        elif figure < guess:
            print ("Wrong. The answer is lower")
        else:
            break

    if figure == guess:
        print("You guessed correctly! You win!")

figure = randomFig()
welcome()
events(figure)