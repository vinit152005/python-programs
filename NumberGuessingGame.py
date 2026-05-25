#number guessing game pyhton program
import random

guesss = 0
number = random.randint(1,100)
is_running = True
while is_running:
    userNumber = int(input("choose a number between 1 and 100: "))
    if userNumber < 1 or userNumber > 100:
        print("number is out of range")
    elif userNumber == number:
        print("you guessed right")
        is_running = False
    elif userNumber < number:
        print("choose higher")

    elif userNumber > number:
        print("choose lower")

    guesss +=1

print(f"{guesss} guesss")
