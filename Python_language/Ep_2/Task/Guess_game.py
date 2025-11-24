# 11. Guessing Game

    # 1.Number guessing game using loops + conditions
    
import random

secret_num = random.randint(1,20)

guess = 0
attempt = 0

while guess != secret_num:
    guess = int(input("Enter the Number :"))
    attempt +=1
    
    if guess > secret_num:
        print("Too High! Please try Again...")
    elif guess < secret_num:
        print("Too Low! Please try Again...")
    else:
        print("You Guessed The Correct Number...")


print(f"You are Guessed the Number in {attempt} Attempt ")
