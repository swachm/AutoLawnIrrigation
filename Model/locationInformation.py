class LocationWeatherData():

    def __init__(self, city="", country="" ,dateTime=0, sunrise=0, sunset=0, currentTemp=0, currentMaxTemp=0,
                 currentMinTemp=0, currentHumidity=0, currentCloudiness=0, rainInLastXHour=0, rainHour = 0,
                 snowInLastXHour=0, snowHour=0, soilMoisture=0, soilTemp=1, totalRainInNext24Hour=0):
        self.city = city
        self.country = country
        self.dateTime = dateTime
        self.sunrise = sunrise
        self.sunset = sunset
        self.currentTemp = currentTemp
        self.currentMaxTemp = currentMaxTemp
        self.currentMinTemp = currentMinTemp
        self.currentHumidity = currentHumidity
        self.currentCloudiness = currentCloudiness
        self.rainInLastXHour = rainInLastXHour
        self.rainHour = rainHour
        self.snowInLastXHour = snowInLastXHour
        self.snowHour = snowHour
        self.soilMoisture = soilMoisture
        self.soilTemp = soilTemp
        self.totalRainInNext24Hour = totalRainInNext24Hour

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = str(value)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = str(value)

    @property
    def dateTime(self):
        return self._dateTime

    @dateTime.setter
    def dateTime(self, value):
        self._dateTime = int(value)

    @property
    def sunrise(self):
        return self._sunrise

    @sunrise.setter
    def sunrise(self, value):
        self._sunrise = int(value)

    @property
    def sunset(self):
        return self._sunset

    @sunset.setter
    def sunset(self, value):
        self._sunset = int(value)

    @property
    def currentTemp(self):
        return self._currentTemp

    @currentTemp.setter
    def currentTemp(self, value):
        self._currentTemp = int(value)

    @property
    def currentMaxTemp(self):
        return self._currentMaxTemp

    @currentMaxTemp.setter
    def currentMaxTemp(self, value):
        self._currentMaxTemp = int(value)

    @property
    def currentMinTemp(self):
        return self._currentMinTemp

    @currentMinTemp.setter
    def currentMinTemp(self, value):
        self._currentMinTemp = int(value)

    @property
    def currentHumidity(self):
        return self._currentHumidity

    @currentHumidity.setter
    def currentHumidity(self, value):
        self._currentHumidity = int(value)

    @property
    def currentCloudiness(self):
        return self._currentCloudiness

    @currentCloudiness.setter
    def currentCloudiness(self, value):
        self._currentCloudiness = int(value)

    @property
    def rainInLastXHour(self):
        return self._rainInLastXHour

    @rainInLastXHour.setter
    def rainInLastXHour(self, value):
        self._rainInLastXHour = int(value)

    @property
    def rainHour(self):
        return self._rainHour

    @rainHour.setter
    def rainHour(self, value):
        self._rainHour = int(value)

    @property
    def snowInLastXHour(self):
        return self._snowInLastXHour

    @snowInLastXHour.setter
    def snowInLastXHour(self, value):
        self._snowInLastXHour = int(value)

    @property
    def snowHour(self):
        return self._snowHour

    @snowHour.setter
    def snowHour(self, value):
        self._snowHour = int(value)

    @property
    def soilMoisture(self):
        return self._soilMoisture

    @soilMoisture.setter
    def soilMoisture(self, value):
        self._soilMoisture = int(value)

    @property
    def soilTemp(self):
        return self._soilTemp

    @soilTemp.setter
    def soilTemp(self, value):
        self._soilTemp= int(value)