student_count = 0
standard_count = 0
kid_count = 0
total_places = 0
while True:
    name = input()
    if name == "Finish":
        break

    place = int(input())

    place_count = 0
    for i in range(1, place + 1):
        ticket = input()
        if ticket == "End":
            print(f"{name} - {(place_count / place * 100):.2f}% full.")
            break

        if ticket == "standard":
            standard_count += 1
            place_count += 1

        if ticket == "student":
            student_count += 1
            place_count += 1

        if ticket == "kid":
            kid_count += 1
            place_count += 1

        if place_count == place:
            print(f"{name} - 100.00% full.")
            break

    total_places += place_count

print(f"Total tickets: {total_places}")
print(f"{(student_count / total_places * 100):.2f}% student tickets.")
print(f"{(standard_count / total_places * 100):.2f}% standard tickets.")
print(f"{(kid_count / total_places * 100):.2f}% kid tickets.")




