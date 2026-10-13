# Secure Login System

# Predefined login credentials
correct_username = "student"
correct_password = "Python@123"

while True:
    print("\n--- SECURE LOGIN SYSTEM ---")

    try:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ")

        # Validate empty inputs
        if username == "" or password == "":
            raise ValueError("Username and password cannot be empty.")

        # Validate login credentials
        if username == correct_username and password == correct_password:
            print("Login Successful! Welcome,", username)
            break
        else:
            print("Invalid username or password.")
            print("Please try again.")

    except ValueError as error:
        print("Input Error:", error)

    except Exception as error:
        print("An unexpected error occurred:", error)