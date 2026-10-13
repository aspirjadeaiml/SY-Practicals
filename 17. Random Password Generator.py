#Develop a Random Password Generator

import random
import string

# Random Password Generator

print("--- RANDOM PASSWORD GENERATOR ---")

length = int(input("Enter password length: "))

if length < 1:
    print("Password length must be at least 1.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)