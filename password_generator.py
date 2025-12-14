import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    char_pool = ''
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    if not char_pool:
        print("Error: No character types selected!")
        return None

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter password length (e.g., 8-32): "))
        if length < 1:
            print("Length must be at least 1.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_letters, use_numbers, use_symbols)
if password:
    print(f"Generated password: {password}")