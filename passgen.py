import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True, include_word=None):
    try:
        character_sets = ''
        if use_lowercase:
            character_sets += string.ascii_lowercase
        if use_uppercase:
            character_sets += string.ascii_uppercase
        if use_digits:
            character_sets += string.digits
        if use_symbols:
            character_sets += "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

        if not character_sets:
            print("No character sets selected. Using default character set.")
            character_sets = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

        password = ''.join(random.choice(character_sets) for _ in range(length))

        if include_word:
            
            index = random.randint(0, length - len(include_word))
            password = password[:index] + include_word + password[index + len(include_word):]

        return password
    except Exception as e:
        print("Error generating password:", e)
        return None

def get_yes_or_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    try:
        length = int(input("Enter the length of the password (default is 12): "))
        use_lowercase = get_yes_or_no_input("Include lowercase letters? (yes/no): ") == 'yes'
        use_uppercase = get_yes_or_no_input("Include uppercase letters? (yes/no): ") == 'yes'
        use_digits = get_yes_or_no_input("Include digits? (yes/no): ") == 'yes'
        use_symbols = get_yes_or_no_input("Include symbols? (yes/no): ") == 'yes'
        include_word = input("Enter a specific word to include in the password (leave blank for none): ")

        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols, include_word)
        if password:
            print("Generated password:", password)
    except ValueError as ve:
        print("Invalid input:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
