import sys
import csv
import tabulate



def main():
    validate_command_line_args()
    print(file_grid())



def validate_command_line_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def file_grid():
    try:
        with open(sys.argv[1], newline="") as file:

            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)

            return tabulate.tabulate(rows, headers = header, tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File not found")



if __name__ == "__main__":
    main()