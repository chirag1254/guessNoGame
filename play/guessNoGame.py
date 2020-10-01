import random

def randomFig():
    figure = random.randint(1, 20)
    return figure

def welcome():
    print ("Welcome to guess the number game! Guess the number between 1 and 20! You have 7 guesses! Take a Guess:")

def events(figure):
    while(guesses<=10):
    if guesses==10 :
        print("Gameover")
        break
    guess = int(input())

    if guess>figure:
        print("Opps thats incorrect\n please try a Smaller no. then it\nNo of gusses left =",9-guesses)
        guesses=guesses+1
        continue
    elif guess< figure:
        print("Opps thats incorrect\n please try a Bigger no. then it\nNo of gusses left =", 9 - guesses)
        guesses = guesses + 1
        continue
    elif guess == figure:
        print(" 'Marvelous'\n You won the game \nYou took ", guesses, "gusses")
        break

figure = randomFig()
welcome()
events(figure)
