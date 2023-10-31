name_of_series = str(input())
episode_duration = int(input())
break_duration = int(input())
lunch_time = break_duration / 8
break_time = break_duration / 4
from math import ceil
time_left = break_duration - break_time - lunch_time
if episode_duration <= time_left:
    free_time = ceil(time_left - episode_duration)
    print(f"You have enough time to watch {name_of_series} "
          f"and left with {free_time} minutes free time.")

else:
    deficit = ceil(episode_duration - time_left)
    print(f"You don't have enough time to watch {name_of_series},"
          f" you need {deficit} more minutes.")
