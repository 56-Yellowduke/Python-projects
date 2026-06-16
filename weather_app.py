import requests

api_key = "1603c26619127ff7e4ec6efcea392503"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()


if data["cod"] ==200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels like:", data["main"]["feels_like"], "°C")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind speed:", data["wind"]["speed"], "m/s")
else:
    print("City not found! Please check the city name and try again ")    