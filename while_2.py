from sys import maxsize
max_number =  maxsize

while True:

    number = input()

    if number == "Stop":
        break
    new_number = int(number)

    if new_number < max_number:
        max_number = new_number

print(max_number)