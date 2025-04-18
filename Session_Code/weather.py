import requests

api_key = "6a12c4cf7448b71fc253c8fcbc89d58f"
city = "Toronto"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# q=CityName → city to search
# appid=API_KEY → your personal API key
# units=metric → Celsius (use imperial for Fahrenheit)

response = requests.get(url)
data = response.json()
#print(data)

print(f"Weather in {city}: {data['weather'][0]['description'].title()}")
print(f"Temperature: {data['main']['temp']}°C")
