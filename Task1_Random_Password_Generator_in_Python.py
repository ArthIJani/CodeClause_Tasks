import random
import string

def generate_password(length, strength):
    if strength == "weak":
        characters = string.ascii_letters
    elif strength == "medium":
        characters = string.ascii_letters + string.digits
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid strength selection.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

length = int(input("Enter the desired length of the password: "))

valid_strengths = ["weak", "medium", "strong"]
strength = input("Enter the desired strength of the password (weak, medium, or strong): ")

while strength not in valid_strengths:
    print("Invalid strength selection. Please try again.")
    strength = input("Enter the desired strength of the password (weak, medium, or strong): ")

password = generate_password(length, strength)

if password:
    print("Generated Password:", password)
