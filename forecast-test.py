import requests
from config import open_weather_token
from vocabulary import weather_vocabulary_fd, weather_vocabulary, days_of_the_week
import datetime
from dateutil import parser

from pprint import pprint

def get_weather_forecast(city, open_weather_token):

    try:
        geo = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={open_weather_token}"
        )
        data2 = geo.json()
        #проверка массива всех данных по координатам
        #pprint(data2)

        lat = data2[0]["lat"]
        lon = data2[0]["lon"]

        wfc = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
        )

        data3 = wfc.json()
        #проверка массива всех данных по прогнозу
        #pprint(data3)

        #завтра какой день недели
        temper = data3["list"][7]["dt_txt"]
        temp = parser.parse(temper)
        temp2 = temp.weekday()
        temp3 = str(temp2)
        if temp3 in days_of_the_week:
            dw_tomorrow = days_of_the_week[temp3]
        else:
            dw_tomorrow = "\n"

        # послезавтра какой день недели
        temper_v2 = data3["list"][15]["dt_txt"]
        temp_v2 = parser.parse(temper_v2)
        temp2_v2 = temp_v2.weekday()
        temp3_v2 = str(temp2_v2)
        if temp3_v2 in days_of_the_week:
            dw_after_tomorrow = days_of_the_week[temp3_v2]
        else:
            dw_after_tomorrow = "\n"

        # послепослезавтра какой день недели
        temper_v3 = data3["list"][23]["dt_txt"]
        temp_v3 = parser.parse(temper_v3)
        temp2_v3 = temp_v3.weekday()
        temp3_v3 = str(temp2_v3)
        if temp3_v3 in days_of_the_week:
            dw_after_after_tomorrow = days_of_the_week[temp3_v3]
        else:
            dw_after_after_tomorrow = "\n"

        # ------------------------------описание погоды завтра в полдень------------------------------
        weather_full_description = data3["list"][7]["weather"][0]["description"]
        weather_description = data3["list"][7]["weather"][0]["main"]
        #если подробное описание есть в словаре - показывает его
        if weather_full_description in weather_vocabulary_fd:
            wd_tomorrow_midday = weather_vocabulary_fd[weather_full_description]
        else:
            # если подробного описания нет в словане - показывает краткое
            weather_description in weather_vocabulary
            wd_tomorrow_midday = weather_vocabulary[weather_description]

        # ------------------------------описание погоды завтра вечером------------------------------
        weather_full_description_ev = data3["list"][9]["weather"][0]["description"]
        weather_description_ev = data3["list"][9]["weather"][0]["main"]
        # если подробное описание есть в словаре - показывает его
        if weather_full_description_ev in weather_vocabulary_fd:
            wd_tomorrow_ev = weather_vocabulary_fd[weather_full_description_ev]
        else:
            # если подробного описания нет в словане - показывает краткое
            weather_description_ev in weather_vocabulary
            wd_tomorrow_ev = weather_vocabulary[weather_description_ev]
        if wd_tomorrow_ev == wd_tomorrow_midday:
            wd_tomorrow_evening = f"тоже {wd_tomorrow_midday}"
        else:
            wd_tomorrow_evening = wd_tomorrow_ev

        # ------------------------------описание погоды послезавтра в полдень------------------------------
        weather_full_description_v2 = data3["list"][15]["weather"][0]["description"]
        weather_description_v2 = data3["list"][15]["weather"][0]["main"]
        # если подробное описание есть в словаре - показывает его
        if weather_full_description_v2 in weather_vocabulary_fd:
            wd_after_tomorrow_midday = weather_vocabulary_fd[weather_full_description_v2]
        else:
            # если подробного описания нет в словане - показывает краткое
            weather_description_v2 in weather_vocabulary
            wd_after_tomorrow_midday = weather_vocabulary[weather_description_v2]

        # ------------------------------описание погоды послезавтра вечером------------------------------
        weather_full_description_ev_v2 = data3["list"][17]["weather"][0]["description"]
        weather_description_ev_v2 = data3["list"][17]["weather"][0]["main"]
        # если подробное описание есть в словаре - показывает его
        if weather_full_description_ev_v2 in weather_vocabulary_fd:
            wd_tomorrow_ev_ev_v2 = weather_vocabulary_fd[weather_full_description_ev_v2]
        else:
            # если подробного описания нет в словане - показывает краткое
            weather_description_ev_v2 in weather_vocabulary
            wd_tomorrow_ev_ev_v2 = weather_vocabulary[weather_description_ev_v2]

        if wd_tomorrow_ev_ev_v2 == wd_after_tomorrow_midday:
            wd_after_tomorrow_evening = f"тоже {wd_after_tomorrow_midday}"
        else:
            wd_after_tomorrow_evening = wd_tomorrow_ev_ev_v2

        # ------------------------------описание погоды послепослезавтра в полдень------------------------------
        weather_full_description_v3 = data3["list"][23]["weather"][0]["description"]
        weather_description_v3 = data3["list"][23]["weather"][0]["main"]
        # если подробное описание есть в словаре - показывает его
        if weather_full_description_v3 in weather_vocabulary_fd:
            wd_after_after_tomorrow_midday = weather_vocabulary_fd[weather_full_description_v3]
        else:
            # если подробного описания нет в словане - показывает краткое
            weather_description_v3 in weather_vocabulary
            wd_after_after_tomorrow_midday = weather_vocabulary[weather_description_v3]

        # ------------------------------описание погоды послепослезавтра вечером------------------------------
        weather_full_description_ev_v3 = data3["list"][25]["weather"][0]["description"]
        weather_description_ev_v3 = data3["list"][25]["weather"][0]["main"]
        # если подробное описание есть в словаре - показывает его
        if weather_full_description_ev_v3 in weather_vocabulary_fd:
            wd_after_after_tomorrow_ev = weather_vocabulary_fd[weather_full_description_ev_v3]
        else:
            # если подробного описания нет в словане - показывает краткое
            weather_description_ev_v3 in weather_vocabulary
            wd_after_after_tomorrow_ev = weather_vocabulary[weather_description_ev_v3]

        if wd_after_after_tomorrow_ev == wd_after_after_tomorrow_midday:
            wd_after_after_tomorrow_evening = f"тоже {wd_after_after_tomorrow_midday}"
        else:
            wd_after_after_tomorrow_evening = wd_after_after_tomorrow_ev

        #температура завтра
        temp_tom = data3["list"][7]["main"]["temp"]
        zero_temp = "0"
        zero_for_compare = float(zero_temp)
        if temp_tom > zero_for_compare:
            temp_tomorrow = f"+{temp_tom}°C"
        else:
            temp_tomorrow = f"{temp_tom}°C"

        # температура послезавтра
        temp_tom_v2 = data3["list"][15]["main"]["temp"]
        zero_temp_v2 = "0"
        zero_for_compare_v2 = float(zero_temp_v2)
        if temp_tom_v2 > zero_for_compare_v2:
            temp_after_tomorrow = f"+{temp_tom_v2}°C"
        else:
            temp_after_tomorrow = f"{temp_tom_v2}°C"

        # температура послепослезавтра
        temp_tom_v3 = data3["list"][23]["main"]["temp"]
        zero_temp_v3 = "0"
        zero_for_compare_v3 = float(zero_temp_v3)
        if temp_tom_v3 > zero_for_compare_v3:
            temp_after_after_tomorrow = f"+{temp_tom_v3}°C"
        else:
            temp_after_after_tomorrow = f"{temp_tom_v3}°C"

        #скорость ветра завтра
        wind_speed_tom = data3["list"][7]["wind"]["speed"]
        wind_speed_tomorrow = round(wind_speed_tom * 3.6)

        # скорость ветра послезавтра
        wind_speed_tom_v2 = data3["list"][15]["wind"]["speed"]
        wind_speed_after_tomorrow = round(wind_speed_tom_v2 * 3.6)

        # скорость ветра послепослезавтра
        wind_speed_tom_v3 = data3["list"][23]["wind"]["speed"]
        wind_speed_after_after_tomorrow = round(wind_speed_tom_v3 * 3.6)


        print(f"Держи прогноз погоды на 3 дня! \n",
              f"\n",
              f"Завтра {dw_tomorrow} \n",
              f"В полдень будет {wd_tomorrow_midday} \n",
              f"Вечером - {wd_tomorrow_evening}\n",
              f"Температура {temp_tomorrow} \n",
              f"Скорость ветра {wind_speed_tomorrow} км/ч \n",
              f"\n",
              f"Послезавтра {dw_after_tomorrow} \n",
              f"В полдень будет {wd_after_tomorrow_midday} \n",
              f"Вечером - {wd_after_tomorrow_evening} \n",
              f"Температура {temp_after_tomorrow} \n",
              f"Скорость ветра {wind_speed_after_tomorrow} км/ч\n",
              f"\n",
              f"{dw_after_after_tomorrow} \n",
              f"В полдень будет {wd_after_after_tomorrow_midday} \n",
              f"Вечером - {wd_after_after_tomorrow_evening} \n",
              f"Температура {temp_after_after_tomorrow} \n",
              f"Скорость ветра {wind_speed_after_after_tomorrow} км/ч\n"
              )

    except:
        print(f"Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather_forecast(city, open_weather_token)


if __name__ == '__main__':
    main()
