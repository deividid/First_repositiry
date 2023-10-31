tshirt = float(input())
ball_sum = float(input())

shorts = tshirt * 0.75
socks = shorts * 0.2
shoes = (tshirt + shorts) * 2
total_sum = tshirt + shorts + socks + shoes
total_sum_with_discount = total_sum * 0.85

if total_sum_with_discount >= ball_sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_with_discount:.2f} lv.")

else:
    money_needed = ball_sum - total_sum_with_discount
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {money_needed:.2f} lv. more.")