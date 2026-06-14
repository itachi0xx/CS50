def main():
    time = input("What time is it? ")
    print(convert(time))

def convert(time):
    hours, minutes = time .strip().split(":")
    time = float(hours) + float(minutes) / 60

    if time >= 7 and time <= 8:
        return "breakfast time"
    elif time >= 12 and time <= 13:
        return "lunch time"
    elif time >= 18 and time <= 19:
        return "dinner time"

main()