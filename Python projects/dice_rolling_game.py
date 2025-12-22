import random

def main():
    while True:
        run = input("Roll the dice? (y/n): ")
        if run == 'y':
            print("(" , random.randint(1, 6) , "," , random.randint(1, 6) , ")")
        elif run == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

main()