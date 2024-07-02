import random
import string

def password(length, complexity):
    if length < 1:
        return "Password length should be at least 1"
    
    # Define the character sets based on the complexity level
    characters = ""
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    # Generate the password using random choices from the character sets
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length for the password: "))

# Prompt the user to specify the desired complexity of the password
print("Complexity levels:")
print("1. Low (only lowercase letters)")
print("2. Medium (lowercase and uppercase letters)")
print("3. High (letters and digits)")
print("4. Very High (letters, digits, and special characters)")
complexity_choice = int(input("Enter the complexity level (1-4): "))

# Generate the password
answer = password(length, complexity_choice)

# Display the generated password
print("Generated Password:", answer)
