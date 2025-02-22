# Основные задания в одной программе (доп. задание в файле 7.3)
import requests
from datetime import datetime, timezone


def task_1():
    city = input("Введите название города: ")
    key = "f48c07d166749ecdc554b4c870a74cbe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        country = result["sys"]["country"]
        temperature = result["main"]["temp"]
        pressure = result["main"]["pressure"]
        humidity = result["main"]["humidity"]
        return f"Погода в городе: {city}, {country}\nТемпература: {temperature} °C \nДавление: {pressure} гПа \nВлажность: {humidity}%"
    else:
        return f"Ошибка: Город не найден!"


def task_2():
    url = "http://api.open-notify.org/iss-now.json"
    astronauts_url = "http://api.open-notify.org/astros.json"

    iss_response = requests.get(url)
    astronauts_response = requests.get(astronauts_url)

    iss_result = iss_response.json()
    astronauts_result = astronauts_response.json()

    location = iss_result["iss_position"]
    time = iss_result["timestamp"]
    astronauts = astronauts_result["people"]
    readable_time = datetime.fromtimestamp(time, timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print(
        f"Текущая информация о местоположении МКС: \nВремя обновления: {readable_time} UTC \nМестоположение МКС: Широта: {location['latitude']}° N, Долгота: {location['longitude']}° E"
    )
    if len(astronauts) > 0:
        astr = []
        print("\nЛюди в космосе:")
        for astronaut in astronauts:
            astr.append(f"- {astronaut['name']} на {astronaut['craft']}")
        return "\n".join(astr)
    else:
        return "Сейчас нет людей в космосе."


while True:
    task = input("1 - Задание №1, 2 - Задание №2, 0 - Выход: ")
    match task:
        case '1':
            print(task_1())
        case '2':
            print(task_2())
        case '0':
            break
        case _:
            print("Wrong type!")
