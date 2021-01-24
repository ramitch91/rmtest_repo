# imports
import collections
import requests


def main():
    show_header()
    # get location
    get_location()
    # convert plain text to json
    # contact weather api
    # display weather conditions for chosen location


def show_header():
    print()
    print("---------------------------------")
    print("     WEATHER CLIENT APP")
    print("---------------------------------")
    print()


def get_location():
    location_text = input("Enter location (eg. Mobile, US): ").lower()
    print(location_text)
    location_split = []
    location_split = location_text.split(",")
    print(location_split)


if __name__ == "__main__":
    main()