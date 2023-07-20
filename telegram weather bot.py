import os
import datetime
import requests
import math
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='6383054752:AAE6dCoItkipN40hYTi8Uyfi1yK2mTuhR_U')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    # def greeting(hour):
    #     if 8 <= hour < 12:
    #         await message.reply(f"Доброе утро!Напиши мне название города и я пришлю сводку погоды")
    #     elif hour >= 12 and hour < 18:
    #         await message.reply(f"Добрый день!Напиши мне название города и я пришлю сводку погоды")
    #     else:
    #         await message.reply(f"Доброй ночи!Напиши мне название города и я пришлю сводку погоды")
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&units=metric&appid=f0c001f47039c4f29a033fbdd14851a6")
        data = response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        real_feel_temp = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        # продолжительность дня
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        # получаем значение погоды
        weather_description = data["weather"][0]["main"]

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            # если эмодзи для погоды нет, выводим другое сообщение
            wd = "Посмотри в окно, я не понимаю, что там за погода..."
        await message.reply(
                            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                            f"Погода в городе: {city}\nТемпература: {math.trunc(cur_temp)}°C\nПо ощущениям: {math.trunc(real_feel_temp)}°C\n {wd}\n"
                            f"Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст\nВетер: {wind} м/с \n"
                            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                            f"Хорошего дня!\U0001F609"
        )
    except:
        await message.reply("Проверьте название города!")


if __name__ == "__main__":
    # С помощью метода executor.start_polling опрашиваем
    # Dispatcher: ожидаем команду /start
    executor.start_polling(dp)
