def main():


    while True:

        try:
            fraction = input("Fraction: ")

            fraction = fraction.split("/")



            n = int(fraction[0])
            d = int(fraction[1])


            if n >= 0 and d > 0:
                if n > d:
                    continue

                percentage = round((n / d) * 100)

                if percentage <= 1:
                    print("E")
                    return

                elif percentage >= 99:
                    print("F")
                    return

                else:
                    print(f"{percentage}%")
                    return


        except ValueError:
            print("d, and n must be an Integers")

        except Exception as err:
            print(f"Something goes wrong {err}")

main()