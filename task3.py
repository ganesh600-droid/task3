import random
import string
def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure the password contains at least one of each type of character
    password = [
        random.choice(string.ascii_uppercase), 
        random.choice(string.ascii_lowercase), 
        random.choice(string.digits), 
        random.choice(string.punctuation)
    ]
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(characters, k=length-4)
    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)
    # Join the list to form the final password string
    return ''.join(password)
# Example usage
if __name__ == "_main_":
    password_length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(password_length))
