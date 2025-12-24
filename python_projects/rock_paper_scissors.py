import random

def show(user, computer):
    if user == 'r':
        print("You chose 🪨")
    elif user == 'p':
        print("You chose 📄")
    elif user == 's':
        print("You chose ✂️")
    if computer == 'r':
        print("Computer chose 🪨"   )
    elif computer == 'p':
        print("Computer chose 📄")
    elif computer == 's':
        print("Computer chose ✂️")

def repeat():
    repeat = input("Continue? (y/n):")
    if repeat == 'y':
        return True
    else:
        print("Thanks for playing!")
        exit()

while True:
    computer_choice = random.choice(['r','p','s'])
    user_choice = input("Rock, paper, or scissors? (r/p/s):")
    if user_choice == computer_choice:
        show(user_choice, computer_choice)
        print("It's a tie!")
        repeat()
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        show(user_choice, computer_choice)
        print("You win!")
        repeat()
    elif (user_choice == 'r' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'r'):
        show(user_choice, computer_choice)
        print("You lose!")
        repeat() 
    else:
        print("Invalid choice!")