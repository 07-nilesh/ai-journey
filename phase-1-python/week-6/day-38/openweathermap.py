import requests

# Precise coordinates for Indore
lat = 22.7177
lon = 75.8586

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

# Open-Meteo returns data inside a 'current_weather' sub-dictionary
indore_temp = data['current_weather']['temperature']
wind_speed = data['current_weather']['windspeed']

print("---------------------------------------------")
print(f"🌍 Live Open-Meteo API Endpoint Response Success!")
print(f"📍 Location: Indore, Madhya Pradesh")
print(f"🌡️  Current Temperature: {indore_temp}°C")
print(f"💨 Wind Speed: {wind_speed} km/h")
print("---------------------------------------------")