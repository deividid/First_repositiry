total_steps = 0
target = 10000
check = False

while True:
    steps = input()
    if steps == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        if total_steps >= target:
            check = True
        break
    total_steps += int(steps)
    if total_steps >= target:
        check = True
        break

if check == True:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - target} steps over the goal!")

else:
    print(f"{target - total_steps} more steps to reach goal.")

