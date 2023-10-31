a = input()
from math import pi
area = 0
if a == "triangle" :
   side = float(input())
   height = float(input())
   area = side * height / 2

elif a == "circle":
    radius = float(input())
    area = radius * radius * pi

elif a == "square":
    side = float(input())
    area = side * side

elif a == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_b * side_a

print(f'{area:.3f}')
