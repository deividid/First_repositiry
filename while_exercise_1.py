book = input()
total = 0

while True:
    new_book = input()
    if new_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {total} books.")
        break

    elif new_book != book:
        total += 1

    elif new_book == book:
        print(f"You checked {total} books and found it.")
        break

