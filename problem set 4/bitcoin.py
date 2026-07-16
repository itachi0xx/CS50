import sys
import requests

def main():

    try:
        if len(sys.argv) == 2:

            number = float(sys.argv[1])

            print(number)

        else:
            sys.exit("Missing command-line argument")

    except ValueError:
            sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=537310cf4509cb36474f0aa15dfb250ea4abcca5ea2aedc49719f45f496ef374")

        response.raise_for_status()

        content = response.json()

        price = content["data"]["priceUsd"]

        price = float(price) * number

        print(f"${price:,.4f}")

    except requests.RequestException:
             print("Can't be reached")


if __name__ == "__main__":
    main()

