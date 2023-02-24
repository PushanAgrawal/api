import requests
from datetime import datetime
response=requests.get(url="http://api.open-notify.org/iss-now.json")
data=response.json()


my_lat=26.45308
my_lon=87.28353

iss_lat=data["iss_position"]["latitude"]
iss_lon=data["iss_position"]["longitude"]


parameter={
    "lat":my_lat,
    "lng":my_lon,
    "formatted":0
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

timr_now=datetime.now()
hour=timr_now.hour
print(hour)