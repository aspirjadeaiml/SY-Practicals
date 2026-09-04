# Eligibility Checker System

marks = float(input("Enter your marks percentage: "))
age = int(input("Enter your age: "))

# Decision making using if, if-else and nested if
if marks >= 50:
    if age >= 17:
        print("You are eligible for admission.")
    else:
        print("You are not eligible because your age is less than 17.")
else:
    print("You are not eligible because your marks are less than 50%.")