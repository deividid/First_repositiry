numb = int(input())
first_sum = 0
second_sum = 0

for i in range(1, 2*numb+1):
    if i <= numb:
        first_half = int(input())
        first_sum += first_half
    else:
        second_half = int(input())
        second_sum += second_half

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")

else:
    print(f"No, diff = {abs(first_sum - second_sum)}")
