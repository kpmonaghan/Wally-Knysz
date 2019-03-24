import random
import sys

min = 1
max = 20

keepGoing = True
numberToGuess = random.randint(min, max)
question = "Please enter a number between 1 and 20: "

while (keepGoing):
    ans = int(input(question))

    if ans == numberToGuess:
        print("Correct!!!  Way to go!  Nice job!")
        keepGoing = False
        sys.exit()
    else:
        print("Oops!  That wasn't it!")

        if ans > numberToGuess:
            print("HINT: You guessed too high!")
        else:
            print("HINT: You guessed too low!")

