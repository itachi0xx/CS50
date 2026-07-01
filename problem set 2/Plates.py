def main():
    plate = input("Plate: ").upper()


    if not plate.isalnum():
        print("invalid")
        return

    if not (2 <= len(plate) <= 6):
            print("invalid")
            return

    if not plate[0:2].isalpha():
                print("invalid")
                return

    for i in range(2 ,len(plate)):
        if plate[i].isdigit():

            if plate[i] == "0":
                print("invalid")
                return

            for j in range(i, len(plate)):
                if not plate[j].isdigit():
                    print("invalid")
                    return
            break

    print("Valid")



main()
