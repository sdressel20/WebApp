import requests

api_key = "f37908b35efdf1d8201b485bd80510ab"
city_name = "Berlin"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(url)
data = response.json()
temperature = data['main']['temp']
humidity = data['main']['humidity']

print (temperature)