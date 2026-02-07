import random

with open('words.txt', 'r') as file:
    WORD_LIST = [line.strip() for line in file.readlines()]

word = random.choice(WORD_LIST)
count = 0

while count < 5:
    user_guess = input("Guess the five letter word: ").strip()
    if user_guess == word:
        print(f"Congratulations! The word was [{word}].")
        break
    elif user_guess != word:
        count += 1
        i = 0
        while i < len(word):
            if user_guess[i] == word[i]:
                print(f"[{user_guess[i]}]" , end="")
            else:
                print("_" , end="")
            i += 1
        print()
        print(f"Incorrect guess. You have {5 - count} attempts left.")
        