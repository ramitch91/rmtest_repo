# Filename: birthday_countdown.py

# imports
import datetime
import sys


def main():
    show_header()
    birthday = get_birthday()
    check_birthday(birthday)


def show_header():
    print()
    print("----------------------------")
    print("  Birthday Countdown App")
    print("----------------------------")
    print()


def get_birthday():
    bd_year_text = input("What year were you born [YYYY]: ")
    bd_year = check_int(bd_year_text)
    bd_month_text = input("What month were you born [MM]: ")
    bd_month = check_int(bd_month_text)
    bd_day_text = input("What day were you born [DD]: ")
    bd_day = check_int(bd_day_text)

    print(f"It looks like you were born on {bd_month}/{bd_day}/{bd_year}")

    birthday = datetime.date(bd_year, bd_month, bd_day)
    return birthday


def check_int(number):
    try:
        return int(number)
    except ValueError as ex:
        print(f"Please enter an integer...exiting")
        sys.exit(1)


def check_birthday(check_date: datetime.date):
    today = datetime.date.today()

    # make the years the same to be able to check only the days difference
    current_year = today.year
    check_date = check_date.replace(current_year)

    delta = check_date - today

    if delta.days == 0:
        print("Happy Birthday!")
    elif delta.days < 0:
        days = 0 - delta.days
        print(f"It looks like your birthday was {days} days ago.")
        print("I hope you enjoyed it.")
    else:
        days = delta.days
        print(f"It looks like your birthday is in {days} days.")
        print("I hope you enjoy it.")


if __name__ == "__main__":
    main()