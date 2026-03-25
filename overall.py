def student_averages(students):
    averages = {}
    for student_id, assignments in students.items():
        if assignments:
            averages[student_id] = round(sum(assignments.values()) / len(assignments))
    return averages


def assignment_averages(students):
    if not students:
        return {}

    totals = {}
    counts = {}

    for assignments in students.values():
        for assignment, grade in assignments.items():
            totals[assignment] = totals.get(assignment, 0) + grade
            counts[assignment] = counts.get(assignment, 0) + 1

    return {assignment: round(totals[assignment] / counts[assignment]) for assignment in totals}
