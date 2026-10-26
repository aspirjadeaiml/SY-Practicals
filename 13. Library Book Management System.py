
# Library Book Record System

books = {}

while True:
    print("\n--- Library Book Record System ---")
    print("1. Add Book")
    print("2. Update Book Details")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books[book_id] = {
            "Title": title,
            "Author": author
        }

        print("Book added successfully!")

    elif choice == "2":
        book_id = input("Enter Book ID to update: ")

        if book_id in books:
            books[book_id]["Title"] = input("Enter new title: ")
            books[book_id]["Author"] = input("Enter new author name: ")
            print("Book details updated successfully!")
        else:
            print("Book ID not found.")

    elif choice == "3":
        print("Exiting Library Book Record System.")
        break

    else:
        print("Invalid choice! Please try again.")