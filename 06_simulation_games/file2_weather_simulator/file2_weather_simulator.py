import random

weather_types = ["Sunny ☀️", "Rainy 🌧️", "Cloudy ☁️", "Stormy ⛈️"]

print("🌦️ Weather Simulation\n")

for day in range(1, 6):
    weather = random.choice(weather_types)
    temperature = random.randint(18, 40)
    print(f"Day {day}: {weather} | Temp: {temperature}°C")
