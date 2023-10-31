allowed_mistakes = int(input())
number_of_mistakes = 0
suma = 0
tasks = 0

while True:
    name = input()
    if name == "Enough":
        print(f"Average score: {suma / tasks: .2f}")
        print(f"Number of problems: {tasks}")
        print(f"Last problem: {last_name}")
        break
    grade = int(input())
    suma += grade
    tasks += 1
    last_name = name

    if grade <= 4:
        number_of_mistakes += 1

    if number_of_mistakes == allowed_mistakes:
        print(f"You need a break, {number_of_mistakes} poor grades.")
        break






