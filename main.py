import random
import string


def title():
    print("H A N G M A N")


def menu():
    return input("Type 'play' to play the game, 'exit' to quit: ")


def get_random_word():
    words = ["python", "java", "kotlin", "javascript", "go", "swift", "pascal"]
    random_word = random.choice(words)
    while '-' in random_word:
        random_word = random.choice(words)

    return random_word.upper()


def hangman():
    word = get_random_word()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letter = set()  # what the user has guessed

    lives = 5

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # print out letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(guessed_letter))

        # print out current word
        word_list = [letter if letter in guessed_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        letter = input('Guess a letter: ').upper()
        if letter in alphabet - guessed_letter:  # valid latter in alphabet
            guessed_letter.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)
                print('')

            else:
                lives -= 1  # takes away a life if wrong
                print('\nYour letter,', letter, 'is not in the word.')

        elif letter in guessed_letter:
            lives -= 1
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


def main():
    title()
    while True:
        select = menu()
        if select == "play":
            hangman()
        elif select == "exit":
            break
        break


if __name__ == '__main__':
    main()
