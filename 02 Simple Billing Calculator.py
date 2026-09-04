# Simple Billing Calculator

item_name = input("Enter item name: ")
price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity: "))

# Arithmetic operator
total_bill = price * quantity

# Relational and logical operators
if total_bill >= 1000:
    discount = total_bill * 0.10
elif total_bill >= 500 and total_bill < 1000:
    discount = total_bill * 0.05
else:
    discount = 0

final_amount = total_bill - discount

# Output
print("\n----- BILL -----")
print("Item:", item_name)
print("Total Bill:", total_bill)
print("Discount:", discount)
print("Final Payable Amount:", final_amount)