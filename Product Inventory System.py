# Product Inventory System

products = []
prices = []

while True:
    print("\n--- Product Inventory System ---")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Sort Products by Price")
    print("5. Update Price")
    print("6. Delete Product")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Add product
    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))

        products.append(name)
        prices.append(price)

        print("Product added successfully.")

    # Display products
    elif choice == 2:
        if len(products) == 0:
            print("No products available.")
        else:
            print("\nProduct Inventory:")
            for i in range(len(products)):
                print(products[i], ":", prices[i])

    # Search product
    elif choice == 3:
        name = input("Enter product name to search: ")

        if name in products:
            index = products.index(name)
            print("Product found!")
            print("Price:", prices[index])
        else:
            print("Product not found.")

    # Sort products by price
    elif choice == 4:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] > prices[j]:
                    prices[i], prices[j] = prices[j], prices[i]
                    products[i], products[j] = products[j], products[i]

        print("Products sorted by price.")

    # Update price
    elif choice == 5:
        name = input("Enter product name: ")

        if name in products:
            index = products.index(name)
            new_price = float(input("Enter new price: "))
            prices[index] = new_price
            print("Price updated successfully.")
        else:
            print("Product not found.")

    # Delete product
    elif choice == 6:
        name = input("Enter product name to delete: ")

        if name in products:
            index = products.index(name)
            products.pop(index)
            prices.pop(index)
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    # Exit
    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")