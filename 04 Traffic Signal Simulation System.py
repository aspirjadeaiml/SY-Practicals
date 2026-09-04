# Traffic Signal Simulation System

signal = input("Enter signal color (Red/Yellow/Green): ").lower()

# Conditional statements and logical operations
if signal == "red":
    print("STOP")
elif signal == "yellow" or signal == "orange":
    print("WAIT")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal color")