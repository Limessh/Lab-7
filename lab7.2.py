# Задание №2
import requests
from datetime import datetime, timezone


def get_text():
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
        print("\nЛюди в космосе:")
        for astronaut in astronauts:
            print(f"- {astronaut['name']} на {astronaut['craft']}")
    else:
        print("Сейчас нет людей в космосе.")


if __name__ == "__main__":
    get_text()