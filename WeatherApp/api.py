import requests
import datetime as dt

class api:
    def __init__(self):
        self.api_key = "a70266fb86f93cb7d50d09dec44247bc"


    def get_info_by_city_name(self,city):
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,self.api_key)).json() #&appid={API key}

        try:
            info = {
                "current_temperature": str(round(data["main"]["temp"] - 273.15, 1)) + "°",
                "weather": data["weather"][0]["main"],
                "humidity": data["main"]["humidity"],
                "sunrise": dt.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%A, %B %d, %Y\n%I:%M:%S %p"),
                "sunset": dt.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%A, %B %d, %Y\n%I:%M:%S %p"),
                "country": data["sys"]["country"]
            }

            return info

        except:
            return 0