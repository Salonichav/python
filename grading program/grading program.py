student_scores ={
    "Harry": 85,
    "Ron": 78,
    "Hermione": 92,
    "Draco": 67,
    "Neville": 73
}
student_grades = {} 
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
        print(student_grades)
    elif score >= 81:
        print(student_grades)
        student_grades[student] = "Exceeds Expectations"
        print(student_grades)
    elif score >= 71:
        print(student_grades)   
        student_grades[student] = "Acceptable"
        print(student_grades)
    else:
        student_grades[student] = "Fail"
        print(student_grades)   