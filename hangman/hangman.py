import random

def choose_word():
    try:
        with open("words.txt", "r") as file:
            words = file.readlines()
            if not words:
                raise ValueError("The file 'words.txt' is empty.")
            return random.choice(words).strip()
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    if word is None:
        return
    
    guessed_letters = []
    attempts = 6

    print("Try to guess the word.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter only")
            continue

        if guess in guessed_letters:
            print("You already guessed that")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong you have {} attempts left.".format(attempts))
            if attempts == 0:
                print("You lost 💀 The word was '{}'.".format(word))
                return
        else:
            print("Correct!")

        if all(letter in guessed_letters for letter in word):
            print("W you got the word '{}'.".format(word))
            return

if __name__ == "__main__":
    hangman()
