#Scientific Calculator Utility
import math

# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Function for Power
def power(a, b):
    return a ** b

# Function for Square Root
def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Square root of a negative number is not supported."

# Function for Sine
def sine(angle):
    return math.sin(math.radians(angle))

# Function for Cosine
def cosine(angle):
    return math.cos(math.radians(angle))

# Function for Tangent
def tangent(angle):
    return math.tan(math.radians(angle))


while True:
    print("\n--- SCIENTIFIC CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "10":
        print("Exiting Scientific Calculator.")
        break

    elif choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            result = power(a, b)

        print("Result:", result)

    elif choice == "6":
        a = float(input("Enter a number: "))
        print("Result:", square_root(a))

    elif choice in ["7", "8", "9"]:
        angle = float(input("Enter angle in degrees: "))

        if choice == "7":
            result = sine(angle)
        elif choice == "8":
            result = cosine(angle)
        else:
            result = tangent(angle)

        print("Result:", result)

    else:
        print("Invalid choice. Please try again.")
