#rain-alert
import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ["OWN_API_KEY"]

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
MY_LAT = -11.461230
MY_LON = 34.020199

parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Remember to bring an umbrella.",
        to='whatsapp:+17149028348'
    )
    print(message.sid)


