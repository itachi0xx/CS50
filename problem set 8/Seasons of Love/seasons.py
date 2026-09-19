import sys
from datetime import date
import inflect


def main():
    # input validation
    try:
        user_input = input("Date of Birth: ")
        birth_date = date.fromisoformat(user_input)
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birth_date)

    p = inflect.engine()

    word = p.number_to_words(minutes)

    print(word)



def calculate_minutes(birth_date):

    today = date.today()

    days = (today - birth_date).days

    minutes = days * 24 * 60

    return minutes

if __name__ == "__main__":
    main()