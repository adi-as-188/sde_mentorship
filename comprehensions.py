celsius_weather = {
    "Mumbai": 29,
    "Delhi": 34,
    "London": 15,
    "New York": 22,
    "Tokyo": 19,
    "Sydney": 12
}

warm_cities_fahrenheit = {city: (temperature * 9 / 5) + 32 for city, temperature in celsius_weather.items() if temperature > 20}
print(warm_cities_fahrenheit)