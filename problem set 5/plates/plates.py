def is_valid(plate):
    plate = plate.upper()

    if not plate.isalnum():
        return False

    if not (2 <= len(plate) <= 6):
        return False

    if not plate[:2].isalpha():
        return False

    for i in range(2, len(plate)):
        if plate[i].isdigit():

            if plate[i] == "0":
                return False

            for j in range(i, len(plate)):
                if not plate[j].isdigit():
                    return False
            break

    return True


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()