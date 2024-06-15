import random
import sys

while True:
    try:
        level = input("Level: ")
        if level.isdigit() == True:
            randomint = random.randint(1,int(level))
            break
    except ValueError:
        pass

while True:
    try:
        guess = input('Guess: ')
        guess = int(guess)
        if guess == randomint:
            sys.exit("Just right!")
        elif guess < randomint:
            print("Too small!")
        elif guess > randomint:
            print("Too large!")
        else:
            pass
    except ValueError:
        pass