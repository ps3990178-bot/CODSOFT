import random
import string

def generate_password(length):
    """
    Generates a random password of a specified length using letters, digits, and symbols.
    """
    # Define the character sets to use for the password complexity
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !, @, #, $, etc.
    
    # Combine all character types into one pool
    all_chars = letters + digits + symbols
    
    # Ensure the password contains at least one of each type for strength
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices from the full pool
    # We subtract 3 because we've already added 3 characters (letter, digit, symbol)
    remaining_length = length - 3
    
    if remaining_length > 0:
        password.extend(random.choices(all_chars, k=remaining_length))
    
    # Shuffle the list of characters to randomize the order
    random.shuffle(password)
    
    # Join the list of characters into a single string
    return "".join(password)

def password_generator_app():
    """
    Handles user input and prints the generated password.
    """
    print("🌟 Password Generator 🌟")
    
    # User Input: Prompt for the desired length
    while True:
        try:
            # We enforce a minimum length of 8 as a standard security practice
            min_length = 8
            length = int(input(f"Enter the desired password length (minimum {min_length}): "))
            
            if length < min_length:
                print(f"Password must be at least {min_length} characters long.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Generate Password
    new_password = generate_password(length)

    # Display the Password
    print("\n--- Generated Strong Password ---")
    print(new_password)
    print("---------------------------------")

# Run the application
if __name__ == "__main__":
    password_generator_app()