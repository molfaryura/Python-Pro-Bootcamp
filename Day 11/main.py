from art import logo

import random

import os

import sys

def black_jack():
    play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if play_or_not == 'n':
        sys.exit()
    os.system('clear')

    print(logo)

    while True:
        user_cards = [random.randint(2, 11) for _ in range(2)]
        computer_cards = [random.randint(2, 11) for _ in range(2)]
        
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if sum(user_cards) == 21 and sum(computer_cards) != 21:
            print('BlackJack! You win.')
            black_jack()
        elif sum(computer_cards) == 21:
            print("Computer's Blackjack! You lose.")
            black_jack()

        if sum(computer_cards) < 16:
            computer_cards.append(random.randint(2, 11))
        
        ask_user = input("Type 'y' to get another card, type 'n' to pass: ")

        if ask_user == 'y':
            user_cards.append(random.randint(2, 11))
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards[user_cards.index(11)] = 1
        elif 11 in computer_cards and sum(user_cards) > 21:
            computer_cards[computer_cards.index(11)] = 1

        print(f"Your final hand: {user_cards} final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

        if sum(user_cards) > sum(computer_cards) and sum(user_cards) < 21:
            print("You win!")
        elif sum(computer_cards) > 21 and sum(user_cards) < 21:
            print("You win")
        elif sum(user_cards) > 21 and sum(computer_cards) > 21:
            print("Draw!")
        elif sum(user_cards) == 21 and sum(computer_cards) != 21:
            print('BlackJack! You win.')
        elif sum(computer_cards) == 21:
            print("Computer's Blackjack! You lose.")
        else:
            print("You lose.")

        black_jack()

black_jack()

