# Library Book Record System

# Dictionary to store book details
book = {
    "name": input("Enter book name: "),
    "author": input("Enter author name: "),
    "price": float(input("Enter book price: "))
}

# Display book details
print("\n----- BOOK RECORD -----")
print("Book Name:", book["name"])
print("Author:", book["author"])
print("Price:", book["price"])

# Update book details
book["name"] = input("\nEnter updated book name: ")

# Display updated record
print("\n----- UPDATED BOOK RECORD -----")
print("Book Name:", book["name"])
print("Author:", book["author"])
print("Price:", book["price"])