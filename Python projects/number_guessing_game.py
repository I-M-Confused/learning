import random

random = random.randint(1,100)
while True:
    number = int(input("Guess the number between 1 and 100:"))
    if number < random:
        print("Too low!")
    elif number > random:
        print("Too high!")
    elif number == random:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Please enter a valid number")