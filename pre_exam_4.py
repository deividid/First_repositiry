students = int(input())
grades_less_than_3 = 0
grades_less_than_4 = 0
grades_less_than_5 = 0
grades_over_5 = 0
total_grades = 0

for i in range(1, students + 1):
    grade = float(input())
    total_grades += grade
    if 2 <= grade <= 2.99:
        grades_less_than_3 += 1

    elif 3 <= grade <= 3.99:
        grades_less_than_4 += 1
    elif 4 <= grade <= 4.99:
        grades_less_than_5 += 1
    elif grade >= 5:
            grades_over_5 += 1

average_grade = total_grades / students

print(f"Top students: {(grades_over_5 / students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(grades_less_than_5 / students * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(grades_less_than_4 / students * 100):.2f}%")
print(f"Fail: {(grades_less_than_3 / students * 100):.2f}%")
print(f"Average: {average_grade:.2f}")