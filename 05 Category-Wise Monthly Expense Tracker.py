# Category-Wise Monthly Expense Tracker

food = 0
travel = 0
shopping = 0
bills = 0
others = 0

while True:
    print("\nCategories: Food, Travel, Shopping, Bills, Others")
    category = input("Enter expense category (or 'stop' to finish): ").lower()

    if category == "stop":
        break

    amount = float(input("Enter expense amount: "))

    # Accumulation logic
    if category == "food":
        food = food + amount
    elif category == "travel":
        travel = travel + amount
    elif category == "shopping":
        shopping = shopping + amount
    elif category == "bills":
        bills = bills + amount
    elif category == "others":
        others = others + amount
    else:
        print("Invalid category")

# Calculate total expense
total_expense = food + travel + shopping + bills + others

print("\n----- MONTHLY EXPENSE REPORT -----")

# Display category-wise expenses
print("Food Expense:", food)
print("Travel Expense:", travel)
print("Shopping Expense:", shopping)
print("Bills Expense:", bills)
print("Others Expense:", others)

print("\nTotal Monthly Expense:", total_expense)