import requests
import datetime
from config import tg_bot_token, open_weather_token
from vocabulary import weather_vocabulary_fd, weather_vocabulary, days_of_the_week
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#обьект "bot", в который кидаем токен
bot = Bot(token=tg_bot_token)
#в aiogram хэндлерами управляет диспетчер, поэтому создаем обьект диспетчера и кидаем ему обьект бота
dp = Dispatcher(bot)

#проверка бота командой старт
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):

    city_buttons = ReplyKeyboardMarkup(row_width=1)

    simf_button = KeyboardButton(text='Симферополь')
    sev_button = KeyboardButton(text='Севастополь')
    yalta_button = KeyboardButton(text='Ялта')
    feo_button = KeyboardButton(text='Феодосия')
    kerch_button = KeyboardButton(text='Керчь')
    evp_button = KeyboardButton(text='Евпатория')

    city_buttons.add(simf_button, sev_button, yalta_button, feo_button, kerch_button, evp_button)

    await message.answer("Привет!\nЧтобы узнать прогноз погоды на 3 дня вперед, выбери один из предложенных городов ниже, или напиши свой город", reply_markup=city_buttons)


@dp.message_handler()
async def get_weather_forecast(message: types.Message):

    try:
        geo = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={message.text}&appid={open_weather_token}"
        )
        data2 = geo.json()
        # проверка массива всех данных по координатам
        # pprint(data2)

        lat = data2[0]["lat"]
        lon = data2[0]["lon"]

        wfc = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
        )

        data3 = wfc.json()
        # проверка массива всех данных по прогнозу
        # pprint(data3)

        today_mark = datetime.date.today()
        today_mark_v2 = today_mark.weekday()

        # ------------------------------ завтра какой день недели -----------------------------------
        tomorrow_mark = today_mark_v2 + 1
        tomorrow_mark_v2 = str(tomorrow_mark)
        if tomorrow_mark_v2 in days_of_the_week:
            tomorrow_comp = days_of_the_week[tomorrow_mark_v2]
        else:
            pass

        # ------------------------------ послезавтра какой день недели ------------------------------
        after_tomorrow_mark = today_mark_v2 + 2
        after_tomorrow_mark_v2 = str(after_tomorrow_mark)
        if after_tomorrow_mark_v2 in days_of_the_week:
            after_tomorrow_comp = days_of_the_week[after_tomorrow_mark_v2]
        else:
            pass

        # ------------------------------ послепослезавтра какой день недели ------------------------------
        after_after_tomorrow_mark = today_mark_v2 + 3
        after_after_tomorrow_mark_v2 = str(after_after_tomorrow_mark)
        if after_after_tomorrow_mark_v2 in days_of_the_week:
            after_after_tomorrow_comp = days_of_the_week[after_after_tomorrow_mark_v2]
        else:
            pass

        date01 = data3["list"][5]["dt_txt"]  # min for correct_tomorrow_mid_time
        date02 = data3["list"][6]["dt_txt"]
        date03 = data3["list"][7]["dt_txt"]
        date04 = data3["list"][8]["dt_txt"]
        date05 = data3["list"][9]["dt_txt"]
        date06 = data3["list"][10]["dt_txt"]
        date07 = data3["list"][11]["dt_txt"]
        date08 = data3["list"][12]["dt_txt"]  # max for correct_tomorrow_mid_time

        mid_time_mark = "12:00:00"
        tomorrow_mark_vv = today_mark + datetime.timedelta(days=1)
        correct_tomorrow_mid_time = f"{tomorrow_mark_vv} {mid_time_mark}"

        if date01 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][5]["main"]["temp"]
            wst = data3["list"][5]["wind"]["speed"]
            wfdt = data3["list"][5]["weather"][0]["description"]
            wdt = data3["list"][5]["weather"][0]["main"]
            wfdte = data3["list"][7]["weather"][0]["description"]
            wdte = data3["list"][7]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][13]["main"]["temp"]
            wst2 = data3["list"][13]["wind"]["speed"]
            wfdt2 = data3["list"][13]["weather"][0]["description"]
            wdt2 = data3["list"][13]["weather"][0]["main"]
            wfdte2 = data3["list"][15]["weather"][0]["description"]
            wdte2 = data3["list"][15]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][21]["main"]["temp"]
            wst3 = data3["list"][21]["wind"]["speed"]
            wfdt3 = data3["list"][21]["weather"][0]["description"]
            wdt3 = data3["list"][21]["weather"][0]["main"]
            wfdte3 = data3["list"][23]["weather"][0]["description"]
            wdte3 = data3["list"][23]["weather"][0]["main"]
        elif date02 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][6]["main"]["temp"]
            wst = data3["list"][6]["wind"]["speed"]
            wfdt = data3["list"][6]["weather"][0]["description"]
            wdt = data3["list"][6]["weather"][0]["main"]
            wfdte = data3["list"][8]["weather"][0]["description"]
            wdte = data3["list"][8]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][14]["main"]["temp"]
            wst2 = data3["list"][14]["wind"]["speed"]
            wfdt2 = data3["list"][14]["weather"][0]["description"]
            wdt2 = data3["list"][14]["weather"][0]["main"]
            wfdte2 = data3["list"][16]["weather"][0]["description"]
            wdte2 = data3["list"][16]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][22]["main"]["temp"]
            wst3 = data3["list"][22]["wind"]["speed"]
            wfdt3 = data3["list"][22]["weather"][0]["description"]
            wdt3 = data3["list"][22]["weather"][0]["main"]
            wfdte3 = data3["list"][24]["weather"][0]["description"]
            wdte3 = data3["list"][24]["weather"][0]["main"]
        elif date03 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][7]["main"]["temp"]
            wst = data3["list"][7]["wind"]["speed"]
            wfdt = data3["list"][7]["weather"][0]["description"]
            wdt = data3["list"][7]["weather"][0]["main"]
            wfdte = data3["list"][9]["weather"][0]["description"]
            wdte = data3["list"][9]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][15]["main"]["temp"]
            wst2 = data3["list"][15]["wind"]["speed"]
            wfdt2 = data3["list"][15]["weather"][0]["description"]
            wdt2 = data3["list"][15]["weather"][0]["main"]
            wfdte2 = data3["list"][17]["weather"][0]["description"]
            wdte2 = data3["list"][17]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][23]["main"]["temp"]
            wst3 = data3["list"][23]["wind"]["speed"]
            wfdt3 = data3["list"][23]["weather"][0]["description"]
            wdt3 = data3["list"][23]["weather"][0]["main"]
            wfdte3 = data3["list"][25]["weather"][0]["description"]
            wdte3 = data3["list"][25]["weather"][0]["main"]
        elif date04 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][8]["main"]["temp"]
            wst = data3["list"][8]["wind"]["speed"]
            wfdt = data3["list"][8]["weather"][0]["description"]
            wdt = data3["list"][8]["weather"][0]["main"]
            wfdte = data3["list"][10]["weather"][0]["description"]
            wdte = data3["list"][10]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][16]["main"]["temp"]
            wst2 = data3["list"][16]["wind"]["speed"]
            wfdt2 = data3["list"][16]["weather"][0]["description"]
            wdt2 = data3["list"][16]["weather"][0]["main"]
            wfdte2 = data3["list"][18]["weather"][0]["description"]
            wdte2 = data3["list"][18]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][24]["main"]["temp"]
            wst3 = data3["list"][24]["wind"]["speed"]
            wfdt3 = data3["list"][24]["weather"][0]["description"]
            wdt3 = data3["list"][24]["weather"][0]["main"]
            wfdte3 = data3["list"][26]["weather"][0]["description"]
            wdte3 = data3["list"][26]["weather"][0]["main"]
        elif date05 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][9]["main"]["temp"]
            wst = data3["list"][9]["wind"]["speed"]
            wfdt = data3["list"][9]["weather"][0]["description"]
            wdt = data3["list"][9]["weather"][0]["main"]
            wfdte = data3["list"][11]["weather"][0]["description"]
            wdte = data3["list"][11]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][17]["main"]["temp"]
            wst2 = data3["list"][17]["wind"]["speed"]
            wfdt2 = data3["list"][17]["weather"][0]["description"]
            wdt2 = data3["list"][17]["weather"][0]["main"]
            wfdte2 = data3["list"][19]["weather"][0]["description"]
            wdte2 = data3["list"][19]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][25]["main"]["temp"]
            wst3 = data3["list"][25]["wind"]["speed"]
            wfdt3 = data3["list"][25]["weather"][0]["description"]
            wdt3 = data3["list"][25]["weather"][0]["main"]
            wfdte3 = data3["list"][27]["weather"][0]["description"]
            wdte3 = data3["list"][27]["weather"][0]["main"]
        elif date06 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][10]["main"]["temp"]
            wst = data3["list"][10]["wind"]["speed"]
            wfdt = data3["list"][10]["weather"][0]["description"]
            wdt = data3["list"][10]["weather"][0]["main"]
            wfdte = data3["list"][12]["weather"][0]["description"]
            wdte = data3["list"][12]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][18]["main"]["temp"]
            wst2 = data3["list"][18]["wind"]["speed"]
            wfdt2 = data3["list"][18]["weather"][0]["description"]
            wdt2 = data3["list"][18]["weather"][0]["main"]
            wfdte2 = data3["list"][20]["weather"][0]["description"]
            wdte2 = data3["list"][20]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][26]["main"]["temp"]
            wst3 = data3["list"][26]["wind"]["speed"]
            wfdt3 = data3["list"][26]["weather"][0]["description"]
            wdt3 = data3["list"][26]["weather"][0]["main"]
            wfdte3 = data3["list"][28]["weather"][0]["description"]
            wdte3 = data3["list"][28]["weather"][0]["main"]
        elif date07 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][11]["main"]["temp"]
            wst = data3["list"][11]["wind"]["speed"]
            wfdt = data3["list"][11]["weather"][0]["description"]
            wdt = data3["list"][11]["weather"][0]["main"]
            wfdte = data3["list"][13]["weather"][0]["description"]
            wdte = data3["list"][13]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][19]["main"]["temp"]
            wst2 = data3["list"][19]["wind"]["speed"]
            wfdt2 = data3["list"][19]["weather"][0]["description"]
            wdt2 = data3["list"][19]["weather"][0]["main"]
            wfdte2 = data3["list"][21]["weather"][0]["description"]
            wdte2 = data3["list"][21]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][27]["main"]["temp"]
            wst3 = data3["list"][27]["wind"]["speed"]
            wfdt3 = data3["list"][27]["weather"][0]["description"]
            wdt3 = data3["list"][27]["weather"][0]["main"]
            wfdte3 = data3["list"][29]["weather"][0]["description"]
            wdte3 = data3["list"][29]["weather"][0]["main"]
        elif date08 == correct_tomorrow_mid_time:
            # ----------------------------------------данные о погоде на завтра----------------------------------------
            tt = data3["list"][12]["main"]["temp"]
            wst = data3["list"][12]["wind"]["speed"]
            wfdt = data3["list"][12]["weather"][0]["description"]
            wdt = data3["list"][12]["weather"][0]["main"]
            wfdte = data3["list"][14]["weather"][0]["description"]
            wdte = data3["list"][14]["weather"][0]["main"]
            # ----------------------------------------данные о погоде на послезавтра------------------------------------
            tt2 = data3["list"][20]["main"]["temp"]
            wst2 = data3["list"][20]["wind"]["speed"]
            wfdt2 = data3["list"][20]["weather"][0]["description"]
            wdt2 = data3["list"][20]["weather"][0]["main"]
            wfdte2 = data3["list"][22]["weather"][0]["description"]
            wdte2 = data3["list"][22]["weather"][0]["main"]
            # --------------------------------------данные о погоде на послепослезавтра---------------------------------
            tt3 = data3["list"][28]["main"]["temp"]
            wst3 = data3["list"][28]["wind"]["speed"]
            wfdt3 = data3["list"][28]["weather"][0]["description"]
            wdt3 = data3["list"][28]["weather"][0]["main"]
            wfdte3 = data3["list"][30]["weather"][0]["description"]
            wdte3 = data3["list"][30]["weather"][0]["main"]
        else:
            pass

        # температура завтра
        zero_temp = "0"
        zero_for_compare = float(zero_temp)
        if tt > zero_for_compare:
            temp_tomorrow = f"+{tt}°C"
        else:
            temp_tomorrow = f"{tt}°C"

        # температура послезавтра
        if tt2 > zero_for_compare:
            temp_after_tomorrow = f"+{tt2}°C"
        else:
            temp_after_tomorrow = f"{tt2}°C"

        # температура послепослезавтра
        if tt3 > zero_for_compare:
            temp_after_after_tomorrow = f"+{tt3}°C"
        else:
            temp_after_after_tomorrow = f"{tt3}°C"

        # скорость ветра завтра
        wind_speed_tomorrow = round(wst * 3.6)

        # скорость ветра послезавтра
        wind_speed_after_tomorrow = round(wst2 * 3.6)

        # скорость ветра послепослезавтра
        wind_speed_after_after_tomorrow = round(wst3 * 3.6)

        # погода завтра днем

        if wfdt in weather_vocabulary_fd:
            wd_tomorrow_midday = weather_vocabulary_fd[wfdt]
        else:
            wdt in weather_vocabulary
            wd_tomorrow_midday = weather_vocabulary[wdt]

        # погода завтра вечером

        if wfdte in weather_vocabulary_fd:
            wd_tomorrow_ev = weather_vocabulary_fd[wfdte]
        else:
            wdte in weather_vocabulary
            wd_tomorrow_ev = weather_vocabulary[wdte]

        if wd_tomorrow_ev == wd_tomorrow_midday:
            wd_tomorrow_evening = f"тоже {wd_tomorrow_midday}"
        else:
            wd_tomorrow_evening = wd_tomorrow_ev

        # погода послезавтра днем

        if wfdt2 in weather_vocabulary_fd:
            wd_after_tomorrow_midday = weather_vocabulary_fd[wfdt2]
        else:
            wdt2 in weather_vocabulary
            wd_after_tomorrow_midday = weather_vocabulary[wdt2]

        # погода послезавтра вечером

        if wfdte2 in weather_vocabulary_fd:
            wd_tomorrow_ev_ev_v2 = weather_vocabulary_fd[wfdte2]
        else:
            wdte2 in weather_vocabulary
            wd_tomorrow_ev_ev_v2 = weather_vocabulary[wdte2]

        if wd_tomorrow_ev_ev_v2 == wd_after_tomorrow_midday:
            wd_after_tomorrow_evening = f"тоже {wd_after_tomorrow_midday}"
        else:
            wd_after_tomorrow_evening = wd_tomorrow_ev_ev_v2

        # погода послепослезавтра днем

        if wfdt3 in weather_vocabulary_fd:
            wd_after_after_tomorrow_midday = weather_vocabulary_fd[wfdt3]
        else:
            wdt3 in weather_vocabulary
            wd_after_after_tomorrow_midday = weather_vocabulary[wdt3]

        # погода послепослезавтра вечером

        if wfdte3 in weather_vocabulary_fd:
            wd_after_after_tomorrow_ev = weather_vocabulary_fd[wfdte3]
        else:
            wdte3 in weather_vocabulary
            wd_after_after_tomorrow_ev = weather_vocabulary[wdte3]

        if wd_after_after_tomorrow_ev == wd_after_after_tomorrow_midday:
            wd_after_after_tomorrow_evening = f"тоже {wd_after_after_tomorrow_midday}"
        else:
            wd_after_after_tomorrow_evening = wd_after_after_tomorrow_ev

        await message.answer(
            f"Держи прогноз погоды на 3 дня! \n \n"
            f"Погода в городе {message.text} \n \n"
            f"Завтра {tomorrow_comp} \n"
            f"В полдень будет {wd_tomorrow_midday} \n"
            f"Вечером - {wd_tomorrow_evening}\n"
            f"Температура {temp_tomorrow} \n"
            f"Скорость ветра {wind_speed_tomorrow} км/ч \n \n"
            f"Послезавтра {after_tomorrow_comp} \n"
            f"В полдень будет {wd_after_tomorrow_midday} \n"
            f"Вечером - {wd_after_tomorrow_evening} \n"
            f"Температура {temp_after_tomorrow} \n"
            f"Скорость ветра {wind_speed_after_tomorrow} км/ч\n \n"
            f"{after_after_tomorrow_comp} \n"
            f"В полдень будет {wd_after_after_tomorrow_midday} \n"
            f"Вечером - {wd_after_after_tomorrow_evening} \n"
            f"Температура {temp_after_after_tomorrow} \n"
            f"Скорость ветра {wind_speed_after_after_tomorrow} км/ч\n"
        )
    except:
        pass


if __name__ == '__main__':
    executor.start_polling(dp)