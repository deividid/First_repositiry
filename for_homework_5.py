num = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, num + 1):
    new_numbers = int(input())
    if i % 2 == 0:
        even_sum += new_numbers

    else:
        odd_sum += new_numbers

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")

else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")
