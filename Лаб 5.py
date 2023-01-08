import requests
from config import open_weather_token

open_weather_token = "84b9147f24ed873a77279eca4061928d"

response = requests.get('http://api.covidtracking.com')
print(response)


def getCovid(date):
    try:
        response = requests.get(f'https://api.covidtracking.com/v1/us/{date}.json')
        data = response.json()

        date = data['date']
        deathIncrease = data['deathIncrease']
        death = data['death']
        hospIncrease = data['hospitalizedIncrease']
        hosp = data['hospitalized']

        print(f'Дата: {date}\nЗаболело в этот день: {hospIncrease}\nВсего заболело за все время: {hosp}\n'
              f'Смертей в этот день: {deathIncrease}\nВсего смертей: {death}\n')

    except Exception as ex:
        print(ex)
        print('Проверьте формат ввода даты')


def getWeather(city, open_weather_token):
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data = response.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        print(f'Погода: {city}\nТемпература: {cur_weather}C\n'
              f'Влажность: {humidity}%\nДавление: {pressure} гПа\nВетер: {wind} м/с\n')

    except Exception as ex:
        print(ex)
        print('Проверьте название города')


while True:
    fact = input('1 - узнать погоду, 2 - узнать статистику по Covid19, 0 - exit: ')
    match fact:
        case '1':
            getWeather(input('Введите название города: '), open_weather_token)
        case '2':
            getCovid(input('Введите желаемую дату в формате YYYYMMDD до 7 марта 2021 года: '))
        case '0':
            break
        case _:
            print("Wrong type!")
