import random

import string

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

print("Welcome to the PyPassword Generator!")

ask_letters = int(input("How many letters would you like in your password?\n"))

ask_symbols = int(input("How many symbols would you like?\n"))

ask_numbers = int(input("How many numbers would you like?\n"))

result = []

for letter in range(ask_letters):
    result.append(random.choice(letters))

for symbol in range(ask_symbols):
    result.append(random.choice(symbols))

for number in range(ask_numbers):
    result.append(random.choice(numbers))

random.shuffle(result)

password = "".join(result)

print(f"Here is your password: {password}")
