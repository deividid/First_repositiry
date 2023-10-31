number = int(input())
number_as_string = str(number)

for first_number in range(1, int(number_as_string[2]) + 1):
    for second_number in range(1, int(number_as_string[1]) + 1):
        for third_number in range(1, int(number_as_string[0]) + 1):
            result = first_number * second_number * third_number
            print(f"{first_number} * {second_number} * {third_number} = {result};")