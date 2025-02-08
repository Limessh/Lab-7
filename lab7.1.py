# Задание №1
import requests


def get_weather(city, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        country = result["sys"]["country"]
        temperature = result["main"]["temp"]
        pressure = result["main"]["pressure"]
        humidity = result["main"]["humidity"]
        print(
            f"Погода в городе: {city}, {country}\nТемпература: {temperature} °C \nДавление: {pressure} гПа \nВлажность: {humidity}%"
        )
    else:
        print(f"Ошибка: Город не найден!")


if __name__ == "__main__":
    city = input("Введите название города: ")
    key = "f48c07d166749ecdc554b4c870a74cbe"
    get_weather(city, key)
