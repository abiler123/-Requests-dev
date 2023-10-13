import requests

api_key = 'ae3fa3935be6bf28e5ac9a4cbd8116d1'

user_input = input("Enter your city:")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod']== '404':
    print("No City Found")
else:
    weather = weather_data.json()["weather"][0]["main"]
    temp = weather_data.json()["main"]["temp"]
    desc = weather_data.json()["weather"][0]["description"]

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")
    print(f"Description: {desc}")