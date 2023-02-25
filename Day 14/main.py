import random

import os

from data import data

from art import logo, vs

score = 0

while True:
    print(logo)

    person1 = random.choice(data)
    person2 = random.choice(data)

    while person1 == person2:
        person2 = random.choice(data)

    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(vs)

    print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
    
    followers = input("Who has more followers? Type'A' or 'B': ").lower()

    compare_followers = person1['follower_count'] > person2['follower_count']

    if followers == 'a' and compare_followers:
        score += 1
        print(score)
    elif followers == 'b' and not compare_followers:
        score += 1
        print(score)
    else:
        os.system('clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

        break
    
    os.system('clear')
