import random
import sys

rock = '''
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ___
---'   __)__
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
'''

rps = {'0':rock, '1':paper, '2':scissors}

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
try:
    shape = rps[user_choice]
    print(shape)
except KeyError:
    print("Yout typed an invalid number, you lose!")
    sys.exit()

print("Computer chose:")
computer_choice = random.choice([rock, paper, scissors])
print(computer_choice)


if shape is computer_choice:
    print("It is a Draw!")
else:
    if ((shape is rock and 
        computer_choice is paper) or 
        (shape is paper and computer_choice is scissors)
        or shape is scissors and computer_choice is rock):
        print("You lose")
    else:
        print("You win!")

