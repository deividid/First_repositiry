weight = int(input())
height = int(input())
width = int(input())
volume = weight * height * width

while True:
    new = input()
    if new == "Done":
        print(f"{volume} Cubic meters left.")
        break

    volume = volume - int(new)

    if volume <= 0:
        print(f"No more free space! You need {abs(volume)} Cubic meters more.")
        break