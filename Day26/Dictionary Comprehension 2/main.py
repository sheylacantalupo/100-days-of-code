import json

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c ) in weather_c.items()}

with open('weather_f', 'w') as fp:
    json.dump(weather_f, fp)



