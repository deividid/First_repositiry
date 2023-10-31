from sys import maxsize

number = int(input())
min_num = maxsize
max_num = - maxsize

for _ in range(number):
    new_number = int(input())

    if new_number < min_num:
        min_num = new_number

    if new_number > max_num:
        max_num = new_number

print(f"Max number: {max_num}")
print(f"Min nmber: {min_num}")
