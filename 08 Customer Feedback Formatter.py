# Customer Feedback Formatter

name = input("Enter customer name: ")
feedback = input("Enter customer feedback: ")

name = name.title()
feedback = feedback.strip().capitalize()

print("\n====================================")
print("        CUSTOMER FEEDBACK")
print("====================================")
print("Customer Name :", name)
print("Feedback      :", feedback)
print("------------------------------------")
print("Thank you,", name)
print("For your valuable feedback!")
print("====================================")