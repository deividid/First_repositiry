people = int(input())
points = float(input())
season = input()
place = input()
prize_money = 0

if place == "Bulgaria":
    if season == "summer":
        prize_money = points * people * 0.95

    elif season == "winter":
        prize_money = points * people * 0.92

elif place == "Abroad":
    if season == "summer":
        prize_money = points * people * 1.5 * 0.9

    elif season == "winter":
        prize_money = points * people * 1.5 * 0.85

donation = 0.75 * prize_money
money_per_person = prize_money * 0.25 / people
print(f"Charity - {donation:.2f}")
print(f"Money per dancer - {money_per_person:.2f}")