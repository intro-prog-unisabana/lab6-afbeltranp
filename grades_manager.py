def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name:\n").strip().title()
    grades = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n").strip()
        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        grades[subject.strip().title()] = float(grade.strip())

    student_grades[name] = grades
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades


def get_students(student_grades, keys):
    found = {}
    normalized_map = {name.lower(): name for name in student_grades}

    for key in keys:
        lookup = key.strip().lower()
        if lookup in normalized_map:
            proper_name = normalized_map[lookup]
            found[proper_name] = student_grades[proper_name]
        else:
            print(f"{key.strip().title()} not found!")

    return found


def avg_by_student(student_grades, keys=None):
    selected_students = student_grades if keys is None else get_students(student_grades, keys)

    for name, grades in selected_students.items():
        if grades:
            average = sum(grades.values()) / len(grades)
        else:
            average = 0.0
        print(f"{name}: {average:.1f}")
