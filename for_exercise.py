hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())
difference_hours = hour_exam - hour_arrival
difference_minutes = minute_exam - minute_arrival

if difference_minutes == 0 and difference_hours == 0:
    print("On time")
else:
    if difference_hours < -1:
        print("Late")
        if difference_hours < -1:
            if difference_minutes > 0:
                if difference_minutes < 10:
                    print(f"{abs(difference_hours)}:0{difference_minutes} hours after the start")

                else:
                    print(f"{abs(difference_hours)}:{difference_minutes} hours after the start")

            else:
                if abs(difference_minutes) > 50:
                    print(f"{abs(difference_hours)-1}:0{60 - abs(difference_minutes)} hours after the start")

                else:
                    print(f"{abs(difference_hours)-1}:{60 - abs(difference_minutes)} hours after the start")

    elif difference_hours == -1:
        print("Late")
        if difference_minutes > 0:

            print(f"{60 - difference_minutes} minutes after the start")


        else:

            if abs(difference_minutes) < 10:
                print(f"{abs(difference_hours)}:0{abs(difference_minutes)} hours after the start")

            else:
                print(f"{abs(difference_hours)}:{abs(difference_minutes)} hours after the start")

    elif difference_hours == 0:

        if difference_minutes < 0:
            print("Late")
            print(f"{abs(difference_minutes)} minutes after the start")

        elif difference_minutes <= 30:
            print(f"On time")
            print(f"{abs(difference_minutes)} minutes before the start")

        elif difference_minutes > 30:
            print("Early")
            print(f"{abs(difference_minutes)} minutes before the start")

    elif difference_hours == 1:
        if difference_minutes <= -30:
            print("On time")
            print(f"{60 - abs(difference_minutes)} minutes before the start")

        elif -30 < difference_minutes < 0:
            print("Early")
            print(f"{60 - abs(difference_minutes)} minutes before the start")

        elif difference_minutes >= 0:
            print("Early")

            if difference_minutes < 10:
                print(f"{difference_hours}:0{difference_minutes} hours before the start")

            else:
                print(f"{difference_hours}:{difference_minutes} hours before the start")

    elif difference_hours > 1:
        print("Early")
        if difference_minutes > 0:
            if difference_minutes < 10:

                print(f"{difference_hours}:0{difference_minutes} hours before the start")

            else:
                print(f"{difference_hours}:{difference_minutes} hours before the start")

        else:
            if abs(difference_minutes) > 50:
                print(f"{difference_hours - 1}:0{60 - abs(difference_minutes)} hours before the start")

            else:
                print(f"{difference_hours - 1}:{60 - abs(difference_minutes)} hours before the start")











