import inflect
def main():
    names = []
    p = inflect.engine()
    try:
        while True:
            name = input("name: ")

            names.append(name)

    except EOFError:

        print(f"\n Adieu, adieu {p.join(names)}")





main()