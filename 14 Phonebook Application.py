# Phonebook Application

phonebook = {}

while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        phonebook[name] = phone
        print("Contact added successfully!")


    elif choice == "2":
        name = input("Enter name to search: ")

        if name in phonebook:
            print("Phone Number:", phonebook[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        print("Exiting Phonebook Application.")
        break

    else:
        print("Invalid choice. Try again.")
