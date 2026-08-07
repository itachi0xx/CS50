import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check the overall format
    if not re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", ip):
        return False

    # Check that each octet is between 0 and 255
    parts = ip.split(".")
    for part in parts:
        if int(part) > 255:
            return False

    return True


if __name__ == "__main__":
    main()