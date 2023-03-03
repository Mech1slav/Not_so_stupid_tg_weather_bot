import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#обьект "bot", в который кидаем токен
bot = Bot(token=tg_bot_token)
#в aiogram хэндлерами управляет диспетчер, поэтому создаем обьект диспетчера и кидаем ему обьект бота
dp = Dispatcher(bot)

button_test = KeyboardButton('Симферополь')
button_test2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_test)

#проверка бота командой старт
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет, напиши мне название города и я пришлю сводку погоды", reply_markup=button_test2)


@dp.message_handler()
async def get_weather(message: types.Message):

    # словарь описания погоды
    weather_vocabulary = {
        "Clear": "Ясно",
        "Clouds": "Облачно",
        "Rain": "Дождь",
        "Drizzle": "Мелкий дождь",
        "Thunderstorm": "Гроза",
        "Snow": "Снег",
        "Mist": "Туман",
        "Fog": "Туман"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        #данные для отображения сводки погоды
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

        #вывод ответа на сводку погоды
        await message.answer(f"Сегодня {datetime.datetime.now().strftime('%d-%m-%Y')}\n"
              f"В городе {city} сейчас {wd}\n"
              f"Температура: {weather_temp}°С\n"
              f"Скорость ветра составляет {wind_speed} м/с\n"
              f"Точное время рассвета {sunrise_timestamp}\n"
              f"Точное время заката {sunset_timestamp}")

    #при неправильном вводе
    except:
        await message.answer("Проверьте название города")

if __name__ == '__main__':
    executor.start_polling(dp)