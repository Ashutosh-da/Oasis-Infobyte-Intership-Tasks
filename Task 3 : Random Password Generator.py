
''' BASIC RANDOM PASSWORD GENERATOR '''



import random
import string

print("Welcome to the Password Generator")

try:
    length = int(input("Enter the password length: "))
    
    if length <= 0:
        print("Password length must be a positive integer.")
        exit()

    use_letters = input("Include alphabets? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
    
    if not any([use_letters, use_numbers, use_symbols]):
        print("You must select at least one character type.")
        exit()
    char_set = ''
    
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    
    if not char_set:
        print("No character types selected. Please select at least one character type.")
        exit()
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    print(f"Generated password: {password}")

except ValueError:
    print("Error: Please enter a valid number for the password length.")
