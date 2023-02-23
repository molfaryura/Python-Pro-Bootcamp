import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

to_continue = True

while to_continue:
     print(f"You have {attempts} attempts remaining to guess the number.")
     guess = int(input("Make a guess: "))

     if guess > number:
         print("Too high!")
     elif guess < number:
         print("Too low!")
     else:
         print("You win!")
         break

     attempts -= 1

     if attempts > 0:
        print("Guess again.")
     else:
         print("You've run out of guesses, you lose.")
         to_continue = False
