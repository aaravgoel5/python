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

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect! You have {} attempts left.".format(attempts))
            if attempts == 0:
                print("You've run out of attempts! The word was '{}'.".format(word))
                return
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word '{}'.".format(word))
            return

if __name__ == "__main__":
    hangman()
