import requests
from config import open_weather_token
from variables import *
from vocabulary import *
import datetime
from pprint import pprint


def main():
    city = input("Введите город: ")
    get_weather_forecast(city, open_weather_token)


if __name__ == '__main__':
    main()
