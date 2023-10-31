grades = 0
not_pass = 0
suma = 0
student_name = input()

while grades < 12:
    if not_pass == 2:
        print(f"{student_name} has been excluded at {grades + 1} grade")
        break
    ocenka = float(input())



    if ocenka < 4:
        not_pass += 1

    else:
        grades += 1
        suma += ocenka

print(f"{student_name} gradueted. Average grade:{suma / 12}")


