from students_methods import *

# Student Data
students = students_loader()


# Main Program Loop
while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add a grade for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input. Please enter a number")
        continue

    if choice == 5:
        students_saver(students)
        print("Exiting program.")
        break
    elif choice == 1:
        student_add(students)
        students_saver(students)
    elif choice == 2:
        grade_add(students)
        students_saver(students)
    elif choice == 3:
        show_report(students)
        students_saver(students)
    elif choice == 4:
        best_student(students)
        students_saver(students)
    else:
        print("Invalid choice!")