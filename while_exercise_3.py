money_vacantion = float(input())
current_money = float(input())
number_of_days = 0
money_needed = current_money - money_vacantion
bad_days = 0

while True:
    action = input()
    amount = float(input())
    number_of_days += 1

    if action == "spend":
        if abs(money_needed)  < amount:
            money_needed = - money_vacantion
        else:
            money_needed -= amount
        bad_days += 1

    elif action == "save":
        money_needed += amount
        bad_days = 0

    if bad_days == 5:
        print(f"You can't save the money.")
        print(number_of_days)
        break

    if money_needed >= 0:
        print(f"You saved the money for {number_of_days} days.")
        break
