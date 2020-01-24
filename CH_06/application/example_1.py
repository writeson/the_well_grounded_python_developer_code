import os
import sys
from typing import Dict, Tuple
from modules import options
from modules import weather
from dotenv import load_dotenv
import colorama
from colorama import Fore, Style


# get things intialized
load_dotenv()
colorama.init()


def format_weather(weather_info: Dict = None, args=None):
    if weather_info:
        print(Fore.LIGHTBLUE_EX + 'Weather Information:' + Fore.LIGHTGREEN_EX)
        print(f'Weather Station Country Code: {weather_info.get("country_code", "NA")}')
        print(f'Weather Station City Name: {weather_info.get("city_name", "NA")}')
        print(f'Weather Station Time Zone: {weather_info.get("timezone", "NA")}')
        print(f'Sunrise: {weather_info.get("sunrise", "NA")}')
        print(f'Sunset: {weather_info.get("sunset", "NA")}')
        print(f'Temperature: {weather_info.get("temp", "NA")}')
        print(f'Fells like: {weather_info.get("app_temp", "NA")}')
        print(f'Wind Direction: {weather_info.get("wind_cdir_full", "NA")}')
        print(f'Description: {weather_info.get("weather", {}).get("description", "NA")}')
        print(Style.RESET_ALL)


def handle_error(error: Tuple = None):
    """Handle an error returned by the weather api call
    
    Keyword Arguments:
        error {Tuple} -- tuple containing the HTTP status and reason (default: {None})
    """
    status_code, reason = error
    print(Fore.RED)
    print(f'Weather request failed, status code: {status_code}, reason: {reason}')
    print(Style.RESET_ALL)
    sys.exit(-1)


def main():

    # get the arguments from the command line
    args = options.get_args(sys.argv[1:])

    # get the weather information
    weather_info = weather.get(
        weather_api_url=os.environ['WEATHER_API_URL'],
        weather_api_key=os.environ['WEATHER_API_KEY'],
        args=args
    )
    # did we get back an error?
    if not isinstance(weather_info, Dict):
        handle_error(error=weather_info)

    # does the user want formatted or raw json?
    if args.format == "text":
        format_weather(weather_info, args)

    # output the json weather information
    else:
        print(weather_info)


if __name__ == "__main__":
    main()
