from art import logo

import string

import time

alphabet = list(string.ascii_uppercase)

def encode(text, shift):
    new_word = []
    for letter in text:
        ind = alphabet.index(letter)
        try:
            new_word.append(alphabet[ind+shift])
        except IndexError:
            new_ind = (ind + shift) % 26
            new_word.append(alphabet[new_ind])

    return (f"Here is the encoded result: {''.join(new_word)}")


def decode(text, shift):
    original_word = []
    for letter in text:
        ind = alphabet.index(letter)
        try:
            original_word.append(alphabet[ind-shift])
        except IndexError:
            new_ind = (ind - shift) % 26
            original_word.append(alphabet[new_ind])

    return (f"Here is the decoded result: {''.join(original_word)}")

print(logo)
time.sleep(0.5)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n").lower()
    text = input("Type your message:\n").upper()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(encode(text=text, shift=shift))
    elif direction == "decode":
        print(decode(text=text, shift=shift))
    else:
        print("Your input is incorrect! Please type 'decode' or encode'")
        break

    ask_user = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()

    if ask_user == 'no':
        print('Bye!')
        break
    elif ask_user == 'yes':
        continue
    else:
        print("Your input is incorrect. Please type 'yes' or 'no'!")
        break
