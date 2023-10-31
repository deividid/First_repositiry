hours = int(input())
minutes = int(input())
new_minutes = minutes + 15 - 60
if minutes < 45:
    minutes = minutes + 15
    print(f"{hours}:{minutes}")

elif hours == 23  and 45 <= minutes < 55:

    print(f"0:0{new_minutes}")

elif hours == 23 and minutes >= 55:
    print(f"0:{new_minutes}")

elif hours < 23 and minutes >=55:
    print(f"{hours + 1}:{new_minutes}")

elif hours < 23 and 45 <= minutes < 55:
    print(f"{hours + 1}:0{new_minutes}")





