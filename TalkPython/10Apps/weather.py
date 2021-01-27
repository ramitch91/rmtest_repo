# imports
import collections
import requests

Location = collections.namedtuple("Location", "city state country")
Weather = collections.namedtuple("Weather", "location units temp condition")


def main():
    show_header()
    # get location
    location_text = input("Enter location (eg. Mobile, US): ")
    # convert plain text to data we can use
    loc = convert_plaintext_location(location_text)
    # contact weather api
    data = call_weather_api(loc)
    # display weather conditions for chosen location
    if data.units == "imperial":
        scale = "F"
    else:
        scale = "C"

    location_name = get_location_name(loc)
    print(f"The weather in {location_name} is {data.temp} {scale} and {data.condition}")


def show_header():
    print()
    print("---------------------------------")
    print("     WEATHER CLIENT APP")
    print("---------------------------------")
    print()


def convert_plaintext_location(location_text: str):
    if not location_text or not location_text.strip():
        return None
    location_text = location_text.lower().strip()
    parts = location_text.split(",")

    city = ""
    state = ""
    country = "us"
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()
    else:
        return None

    return Location(city, state, country)


def call_weather_api(loc):
    url = f"https://weather.talkpython.fm/api/weather?city={loc.city}&country={loc.country}&units=imperial"
    if loc.state:
        url += f"&state={loc.state}"

    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Error: {resp.text}")
        return None

    data = resp.json()
    return convert_api_weather(loc, data)


def convert_api_weather(loc, data):
    temp = data.get("forecast").get("temp")
    w = data.get("weather")
    condition = f"{w.get('category')}: {w.get('description').capitalize().strip()} "
    weather = Weather(loc, "imperial", temp, condition)
    return weather


def get_location_name(location):
    if not location.state:
        return f"{location.city.capitalize()}, {location.country.upper()}"
    else:
        return f"{location.city.capitalize()}, {location.state.upper()}, {location.country.upper()}"


if __name__ == "__main__":
    main()