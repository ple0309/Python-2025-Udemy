#---------------------------- Practice ---------------------------------
# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

# #If we want to get the value of the key we can do like this below.
# data = response.json()["iss_position"]
# print(data)

#Status code will be 200
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")

# #However if the url does not exist. It will be 404. URL below is missed 's'.
# #It should be .../iss-now.json.
# response = requests.get(url="http://api.open-notify.org/is-now.json")
# print(response.status_code)

#---------------------------- Response code ----------------------------
#1XX: hold on, processing.
#2XX: Here we go. Successful.
#3XX: Go away. Don't actually have permission.
#4XX: You screwed up. The thing you're looking for doesn't exist.
#5XX: I screwed up. maybe the server down.
#-----------------------------------------------------------------------

#---------------------------- Sunrise and Sunset -----------------------
import requests
from datetime import datetime

#Getting the lat and long from latlong.net (longitude and latitude)
#Los Angeles, US
MY_LAT = 34.052235
MY_LONG = -118.243683

#Parameter is required in sunrise and sunset below.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, #formatted will turn off and on 24 style hours.
}

#params for parameters
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

#The split function will split the date and hours into two part with "T" between.
#Then [1] will get the part of Hour.
#Still split hours and minutes by ":"
#Then [0] will return the hours part.
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

