from art import *

from random_word import RandomWords

r = RandomWords()
                                                                    
chosen_word = r.get_random_word()
print(f'Letter is {chosen_word}')

display = ['_' for _ in range(len(chosen_word))]

lives = 6

print(logo)

while True:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose one life.")
    else:
        print(" ".join(display))

    print(stages[lives])

    if "".join(display) == chosen_word and lives > 0:
         print('You win.')
         break
    elif lives == 0:
        print('You lose')
        break
    else:
        continue
