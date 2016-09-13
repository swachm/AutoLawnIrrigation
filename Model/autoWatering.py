#!/usr/bin/python
import time
import math
import datetime
from Model.recordData import RecordData
from Model.httpRequest import httpRequest
from Model.lawn import LawnProperties

class AutoWatering():

    def __init__(self, lawn, data):
        self.lawn = lawn
        self.data = data

    #add variable to incorporate the duration of the water and check server setting around 7 or 8

    def shouldWater(self):
        #serverWeatherConnection = httpRequest(self.lawn)
        #data = serverWeatherConnection.parseCurrentData()

        localTime = datetime.datetime.now()
        recodingAllData = RecordData()

        print(localTime)

        lastTimeWatered = 1 #Make a call to a server to check when this particular lawn was watered last time
        timeToRun = 30 #min

        waterringTimeEvening = localTime.replace(hour=19, minute=0, second=0, microsecond=0)
        stopWateringTimeEvening = localTime.replace(hour=19, minute=timeToRun, second=0, microsecond=0)
        waterringTimeMorning = localTime.replace(hour=6, minute=0, second=0, microsecond=0)
        stopWaterringTimeMorning = localTime.replace(hour=6, minute=timeToRun, second=0, microsecond=0)

        if localTime >= waterringTimeEvening and localTime <= stopWateringTimeEvening or localTime >= waterringTimeMorning and localTime >=stopWaterringTimeMorning:
            if self.data.currentTemp > 288.15:
                if lastTimeWatered > 3:
                    if self.data.rainInLastXHour == 0 and self.data.rainHour < 24:
                        if self.data.totalRainInNext24Hour <=13:
                            lastTime  = self.lastTimeLawnRecievedWater()
                            if lastTime > 48:
                                return True
                            else:
                                return False
        else:
            recodingAllData.logWeatherDataforLawn(self.data)
            return False

    def lastTimeLawnRecievedWater(self):
        return