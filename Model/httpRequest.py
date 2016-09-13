from Model.lawn import LawnProperties
from Model.locationInformation import LocationWeatherData
import urllib.request
import json

class httpRequest():
    """docstring for httpRequest"""
    appid = "9d2d320fe2b666687a88e6f323077b95"
    currentDataURL = "http://api.openweathermap.org/data/2.5/weather?q="
    forcastDataURL = "http://api.openweathermap.org/data/2.5/forecast?q="

    def __init__(self, lawn,currentURL="",forcastURL=""):
        self.lawnInfo = lawn
        self.currentURL = str(self.currentDataURL) + str(self.lawnInfo.city) + "," + str(self.lawnInfo.country) + "&appid="+str(self.appid)
        self.forcastURL = str(self.forcastDataURL) + str(self.lawnInfo.city) + "," + str(self.lawnInfo.country) + "&appid="+str(self.appid)

    def parseToJson(self, link):
        response = urllib.request.urlopen(link).read()
        decodedResponse = response.decode('utf8')
        data = json.loads(decodedResponse)
        return data

    def makeCurrentURLRequest(self):
        return self.parseToJson(self.currentURL)

    def makeForcastURLRequest(self):
        return self.parseToJson(self.forcastURL)

    def parseCurrentData(self):
        currentData = self.makeCurrentURLRequest()
        forcastData = self.makeForcastURLRequest()
        sunrise = currentData['sys']['sunrise']
        sunset = int(currentData['sys']['sunset'])
        dateTime = int(currentData['dt'])
        currentTemp = int(currentData['main']['temp'])
        currentMaxTemp = int(currentData['main']['temp_max'])
        currentMinTemp = int(currentData['main']['temp_min'])
        currentHumidity = int(currentData['main']['humidity'])
        currentCloudiness = int(currentData['clouds']['all'])
        rainInLastXHour = 0
        rainHour= 0
        snowInLastXHour = 0
        snowHour = 0

        if 'rain' not in currentData:
            rainInLastXHour = 0
        else:
            rainInLastXHour = (currentData['rain'])  # {Xhr,Xmm}
            key = list(rainInLastXHour.keys())
            rainHour = str(key[0])
            rainInLastXHour = int((currentData['rain'][rainHour]))
            rainHour = int(rainHour)

        if 'snow' not in currentData:
            snowInLastXHour = 0
        else:
            snowInLastXHour = (currentData['snow'])  # {Xhr,Xmm}
            key = list(rainInLastXHour.keys())
            snowHour = str(key[0])
            snowInLastXHour = (currentData['snow'][snowHour])
            snowHour = int(snowHour)

        i = 0
        totalRainInNext24Hour = 0
        for item in (forcastData['list']):
            i = i + 1
            if (i > 6):
                break
            else:
                if 'rain' not in item:
                    totalRainInNext24Hour = 0
                else:
                    if item['rain']:
                        totalRainInNext24Hour = totalRainInNext24Hour + (item['rain']['3h'])

        soilMoisture = 1
        soilTemp = 1
        locationWeatherData = LocationWeatherData(self.lawnInfo.city, self.lawnInfo.country, dateTime,
                                                  sunrise, sunset, currentTemp, currentMaxTemp, currentMinTemp,
                                                  currentHumidity, currentCloudiness, rainInLastXHour, rainHour,
                                                  snowInLastXHour, snowHour, soilMoisture, soilTemp, totalRainInNext24Hour)
        return locationWeatherData