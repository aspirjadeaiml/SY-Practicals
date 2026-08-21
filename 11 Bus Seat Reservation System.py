# Bus Seat Reservation

seats = [
    ["A", "A", "A"],
    ["A", "A", "A"],
    ["A", "A", "A"]
]

# Display seats
print("Bus Seats:")

for i in range(3):
    print(seats[i])

# Reserve a seat
row = int(input("Enter row number (1-3): "))
seat = int(input("Enter seat number (1-3): "))

if seats[row - 1][seat - 1] == "A":
    seats[row - 1][seat - 1] = "R"
    print("Seat Reserved!")
else:
    print("Seat Already Reserved!")

# Display updated seats
print("Updated Seats:")

for i in range(3):
    print(seats[i])
    