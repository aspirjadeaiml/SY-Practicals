# Star and Number Pattern Programs

# ----- STAR PATTERNS -----

print("Star Pattern 1")
for i in range(5):
    print("*")

print("\nStar Pattern 2")
for i in range(1, 6):
    print("*" * i)

print("\nStar Pattern 3")
for i in range(5, 0, -1):
    print("*" * i)

print("\nStar Pattern 4")
for i in range(5):
    print("*****")

print("\nStar Pattern 5")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)


# ----- NUMBER PATTERNS -----

print("\nNumber Pattern 1")
for i in range(1, 6):
    print(i)

print("\nNumber Pattern 2")
for i in range(1, 6):
    print(str(i) * i)

print("\nNumber Pattern 3")
for i in range(1, 6):
    print("12345")

print("\nNumber Pattern 4")
for i in range(5, 0, -1):
    print(str(i) * i)

print("\nNumber Pattern 5")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()