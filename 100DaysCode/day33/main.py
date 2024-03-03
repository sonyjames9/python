import datetime
import requests
import smtplib
import time

MY_EMAIL = "aawrashopping@gmail.com"
PASSWORD = "zqff xnic bhkq swyt"
LAT = '18.6337118'
LNG =  '73.8140685'
TIME_ZONE = "Asia/Kolkata"

def is_iss_overhead():
  response = requests.get(url ="http://api.open-notify.org/iss-now.json")
  response_json = response.json()
  longitude = float(response_json["iss_position"]["longitude"])
  latitude = float(response_json["iss_position"]["latitude"])
  iss_position = (longitude, latitude)

  print(iss_position)
  print(response_json["iss_position"])

  # Check my position is near to ISS position

  if LAT-5 <= latitude <= LAT+5 and LNG-5 <= longitude <= LNG+5:
    return True

def is_night(): 
  sun_url = "https://api.sunrise-sunset.org/json"

  parameters = {
    "lat": LAT,
    "lng": LNG,
    "tzid": TIME_ZONE,
    "formatted": 0
  }

  response  = requests.get(sun_url, params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = data["results"]["sunrise"]
  sunset = data["results"]["sunset"]
  sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
  sunset_hour = int(sunset.split("T")[1].split(":")[0])

  print(data)

  print(f"Sunrise : {sunrise}")
  print(f"Sunset : {sunset}")
  print(f"sunrise_hour : {sunrise_hour}")
  print(f"sunset_hour : {sunset_hour}")

  time_now = datetime.now().hour
  if time_now >= sunset or time_now <= sunrise:
    return True


while True:
  time.sleep(60)
  if is_iss_overhead() and is_night():
      with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
          from_addr=MY_EMAIL, 
          to_addrs=MY_EMAIL, 
          msg="Subject : Look up ISS is above in the sky")
