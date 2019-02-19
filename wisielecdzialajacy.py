import random
from typing import List

words = []
for line in open('words.txt', 'r').readlines():
    words.append(line.strip())

guess_word = []
secret_word = random.choice(words)
lenght_word = len(secret_word)
letters = 'abcdefghijklmopqrstuvwxyz'
letter_storage = []


def print_guess_word(letters: List):
    print('Word to guesss: {0}'.format(''.join(letters)))


def print_attempt_taken(current: int, total: int):
    print('Your attempts', current, '/', total)


def beginning():
    print('Hello new chosen one!\n')
    while True:
        name = input('Your name?\n')
        if name == '':
            print('Just write your name!\n')
        else:
            break


def ask_for_play():
    print('Today is a good day to play some game!\n')
    while True:
        game_choice = input('You want play? y/n\n').lower()
        if game_choice == 'y':
            break
        elif game_choice == 'n':
            exit('Cya latter then!')
        else:
            print('Plese answer only y or n\n')
            continue


def prepare_secret_word():
    for character in secret_word:
        guess_word.append("_")
    print('So the word You need find have', lenght_word, 'characters')
    print('You have 8 attempts\n')
    print('You can enter only 1 letter from a-z\n\n')
    print_guess_word(guess_word)


def game():
    attempts_taken = 1
    max_attempts = 8
    print_attempt_taken(attempts_taken, max_attempts)

    while attempts_taken < max_attempts:
        guess = input('Pick a letter\n').lower()
        if not guess in letters:
            print('Enter a letter from a-z')
        elif guess in letter_storage:
            print('You choosen this letter once! Take another letter!')
        else:
            letter_storage.append(guess)
            if guess in secret_word:
                print('You guessed correctly!')
                for i in range(0, lenght_word):
                    if secret_word[i] == guess:
                        guess_word[i] = guess
                print_guess_word(guess_word)
                print_attempt_taken(attempts_taken, max_attempts)
                if not '_' in guess_word:
                    print('You won!')
                    break
            else:
                print('Letter is not in the word. Try Again!')
                attempts_taken += 1
                print_attempt_taken(attempts_taken, max_attempts)
                if attempts_taken == 8:
                    print("Sorry Mate, You lost like a noob! The word was: {0}".format(secret_word))
                    print('Thank you for your try!')


if __name__ == '__main__':
    beginning()
    ask_for_play()
    prepare_secret_word()
    game()
