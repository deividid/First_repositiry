a = int(input())
bonus = 0
if a <= 100:
   bonus = 5

elif a <= 1000:
    bonus= a * 0.2

else:
    bonus = a * 0.1

if a % 2 == 0:
    bonus = bonus +1

elif a % 5 == 0:
    bonus = bonus + 2

final = a + bonus
print(bonus)
print(final)