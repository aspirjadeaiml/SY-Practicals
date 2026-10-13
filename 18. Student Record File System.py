# Student Record File System

while True:
    print("\n--- STUDENT RECORD SYSTEM ---")
    print("1. Add Student Record")
    print("2. Display All Student Records")
    print("3. Search Student Record")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        course = input("Enter Course Name: ")
        marks = input("Enter Marks: ")

        with open("students.txt", "a") as file:
            file.write(roll_no + "," + name + "," + course + "," + marks + "\n")

        print("Student record saved successfully!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                records = file.readlines()

                if records:
                    print("\n--- ALL STUDENT RECORDS ---")
                    for record in records:
                        print(record.strip())
                else:
                    print("No student records found.")

        except FileNotFoundError:
            print("Student record file does not exist yet.")

    elif choice == "3":
        search_roll = input("Enter Roll Number to search: ")
        found = False

        try:
            with open("students.txt", "r") as file:
                for record in file:
                    details = record.strip().split(",")

                    if details[0] == search_roll:
                        print("\nStudent Found")
                        print("Roll Number:", details[0])
                        print("Name:", details[1])
                        print("Course:", details[2])
                        print("Marks:", details[3])
                        found = True
                        break

            if not found:
                print("Student record not found.")

        except FileNotFoundError:
            print("Student record file does not exist yet.")

    elif choice == "4":
        print("Exiting Student Record System.")
        break

    else:
        print("Invalid choice. Please try again.")