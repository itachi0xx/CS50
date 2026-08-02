import sys


def validate_command_line_args():

    if len(sys.argv) < 2:
       sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
       sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def count_lines():
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                if line.strip().startswith("#"):
                    continue
                if len(line.strip()) == 0:
                    continue
                else:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():

    validate_command_line_args()
    print(count_lines())


if __name__ == "__main__":
    main()