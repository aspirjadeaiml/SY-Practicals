# Banking Menu System

balance = 1000.0

# Function to Deposit Money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
        print("Updated Balance: Rs.", balance)
    else:
        print("Please enter a valid amount.")

# Function to Withdraw Money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully!")
        print("Remaining Balance: Rs.", balance)
    else:
        print("Insufficient balance.")

# Function to Check Balance
def check_balance():
    print("Available Balance: Rs.", balance)

# Main Function
def main():
    while True:
        print("\n--- BANKING MENU SYSTEM ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Balance Inquiry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Calling the Main Function
main()
