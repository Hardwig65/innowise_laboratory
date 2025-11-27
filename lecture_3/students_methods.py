import json

# Stores the current student dataset into a JSON file
def students_saver(students, filename="students_list.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)

# Loads the student dataset from a JSON file (returns empty list if missing)
def students_loader(filename="students_list.json") -> list[dict]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Adds a new student to the list (ensures uniqueness and valid name)
def student_add(students) -> None:
    while True:

        name = input("Enter student name: ").strip().title()
        if not name:
            print("Name cannot be empty.")
            continue
        if any(student["name"] == name for student in students):
            print("This name is already exist")
            continue

        new_person = {"name": name, "grades": []}
        students.append(new_person)
        break

# Appends grades for an existing student
def grade_add(students) -> None:
    name = input("Enter student name: ").title()
    if any(student["name"] == name for student in students):
        for student in students:
            if student["name"] == name:
                while True:
                    user_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
                    if user_input == "done":
                        break
                    try:
                        grade = int(user_input)
                    except ValueError:
                        print("Invalid input. Please enter a number")
                        continue

                    if grade > 100 or grade < 0:
                        print("Invalid input. Please enter a number")
                        continue
                    else:
                        student["grades"].append(grade)
    else:
        print("Student is not found")

# Prints each student's average and overall class statistics
def show_report(students) -> None:
    print("--- Student Grade Analyzer ---")
    students_average = []
    if len(students) == 0:
        print("There is no students")
    else:
        for student in students:
            try:
                average = sum(student["grades"]) / len(student["grades"])
                print(f"{student["name"]}'s average grade is {average:.1f}")
                students_average.append(average)
            except ZeroDivisionError:
                print(f"{student["name"]}'s average grade is N/A")
        print("--------------------------")
        if students_average:
            print(f"Max Average: {max(students_average):.1f}")
            print(f"Min Average: {min(students_average):.1f}")
            print(f"Overall Average: {sum(students_average) / len(students_average):.1f}")
        else:
            print("No grades to calculate statistics.")


# Determines the student with the highest average grade
def best_student(students) -> None:
    if not students:
        print("There are no students.")
        return

    students_with_grades = [s for s in students if s["grades"]]

    if not students_with_grades:
        print("No student has grades yet. Top student cannot be determined.")
        return

    top_student = max(
        students_with_grades,
        key=lambda student: sum(student["grades"]) / len(student["grades"])
    )

    average = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The student with the highest average is {top_student["name"]} with a grade of {average:.1f}")