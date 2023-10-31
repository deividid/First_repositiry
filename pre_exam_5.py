days = 1
meters_till_summit = 8848 - 5364

while True:
    night_rest = input()

    if night_rest == "Yes":
        days += 1

    if days > 5 or night_rest == "END":
        print(f"Failed!")
        print(f"{8848 - meters_till_summit}")
        break

    meters_for_today = int(input())
    meters_till_summit -= meters_for_today

    if meters_till_summit <= 0:
        print(f"Goal reached for {days} days!")
        break
