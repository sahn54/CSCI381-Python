# Name | midterm | Final | Average | Deviation

with open("Class_10/qc_grade.txt") as grade_file:
    list_grades = grade_file.read()
    grades = list_grades.splitlines()
    print(grades)
    for students in grades:
        print(list(students))
    #     for grade in students:
