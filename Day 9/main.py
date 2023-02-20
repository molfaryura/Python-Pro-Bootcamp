from art import logo

import os

participants = dict()

print(logo)
print("Welcome to the secret auction program.")

while True:
    user_name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))

    participants[user_name] = bid

    ask = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if ask == 'yes':
        os.system('clear')
        continue
    else:
        winner = max(participants, key=participants.get)
        print(f"The winner is {winner} with a bid of ${participants[winner]}.")
        break
