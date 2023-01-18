import requests
import smtplib


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f73c4aaeaa404bb1325bdff17e844b1a"
my_email = ""
password = ""

weather_params = {
    "lat": "-7.146335",
    "lon": "-34.835357",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slices = weather_data["list"][:12]

will_rain = False
for hour_data in weather_slices:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,

                            msg=f"Subject:Atencao!!...\n\nLevar um guarda-chuvas")
#print(weather_data["list"][0]["weather"][0]["id"])
# verificar se está rodando
# print(response.status_code)

