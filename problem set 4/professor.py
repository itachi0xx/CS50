import random

def main():

    level = get_level()


    score = 0

    for problem in range(10):
        x, y = generate_integer(level)
        for attemps in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score = {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 1 <= level <= 3:
                break
            else:
                print("Level must be between 1 and 3.")

        except ValueError:
            print("Enter valid number")

    return level

def generate_integer(level):

    x = random.randint(10**(level-1), 10**level - 1)
    y = random.randint(10**(level-1), 10**level - 1)

    if x < y:

        x, y  = y, x

    return x, y



main()