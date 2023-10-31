first_time = int(input())
second_time = int(input())
trird_time = int(input())
combine_time = first_time + second_time + trird_time
minutes = combine_time / 60
seconds = combine_time % 60
from math import floor
minutes = floor(minutes)
if seconds < 10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")