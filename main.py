import requests
import datetime
from config import open_weather_token
from pprint import pprint


def get_weather(city, open_weather_token):
    # словарь определений погоды
    weather_vocabulary = {
        "Clear": "Ясно",
        "Clouds": "Облачно",
        "Rain": "Дождь",
        "Drizzle": "Мелкий дождь",
        "Thunderstorm": "Гроза",
        "Snow": "Снег",
        "Mist": "Туман"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        # город
        city = data["name"]

        # температура воздуха
        weather_temp = data["main"]["temp"]

        # скорость ветра
        wind_speed = data["wind"]["speed"]

        # время рассвета
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        # время заката
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        # погода
        weather_description = data["weather"][0]["main"]
        if weather_description in weather_vocabulary:
            wd = weather_vocabulary[weather_description]
        else:
            wd = "Погода какая-то странная"

        print(f"Сегодня {datetime.datetime.now().strftime('%d-%m-%Y')}\n"
              f"В городе {city} сейчас {wd}\n"
              f"Температура: {weather_temp}°С\n"
              f"Скорость ветра составляет {wind_speed} м/с\n"
              f"Точное время рассвета {sunrise_timestamp}\n"
              f"Точное время заката {sunset_timestamp}")

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
