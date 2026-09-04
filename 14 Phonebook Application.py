# Phonebook Application

phonebook = {}

# Store contacts
name = input("Enter contact name: ")
number = input("Enter phone number: ")

phonebook[name] = number

# Display contact
print("\n----- PHONEBOOK -----")
print("Name:", name)
print("Phone Number:", phonebook[name])