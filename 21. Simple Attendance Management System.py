# Simple Attendance Management System

attendance_list = []

def mark_attendance():
    roll_no = input("Enter student roll number: ")
    name = input("Enter student name: ")

    print("Select Attendance Status:")
    print("P - Present")
    print("A - Absent")

    status = input("Enter P or A: ").upper()

    if status == "P":
        status = "Present"
    elif status == "A":
        status = "Absent"
    else:
        print("Invalid attendance status!")
        return

    # Store student details in a dictionary
    student = {
        "Roll No": roll_no,
        "Name": name,
        "Status": status
    }

    # Add dictionary to the list
    attendance_list.append(student)

    # Save attendance details in a file
    with open("attendance.txt", "a") as file:
        file.write(
            roll_no + "," + name + "," + status + "\n"
        )

    print("Attendance recorded successfully!")


def display_attendance():
    try:
        with open("attendance.txt", "r") as file:
            print("\n--- Student Attendance Records ---")

            records = file.readlines()

            if not records:
                print("No attendance records found.")
                return

            for record in records:
                details = record.strip().split(",")

                if len(details) == 3:
                    print("Roll No:", details[0])
                    print("Name:", details[1])
                    print("Status:", details[2])
                    print("----------------------")

    except FileNotFoundError:
        print("No attendance file found.")


def main():
    while True:
        print("\n===== Attendance Management System =====")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            display_attendance()
        elif choice == "3":
            print("Exiting Attendance Management System.")
            break
        else:
            print("Invalid choice! Please try again.")


main()