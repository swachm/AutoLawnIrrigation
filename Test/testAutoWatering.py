import unittest
import datetime

from Model.autoWatering import AutoWatering
from Model.httpRequest import LocationWeatherData
from Model.lawn import LawnProperties

class testAutoWatering(unittest.TestCase):
    locationWeatherData1 = LocationWeatherData("Vancouver", "Canada", 1473798382,
                                              1471698761, 1471749451, 293.77, 298.71, 289.15,
                                              64, 0, 0.12, 2,
                                              0, 0, 1, 1, 0.45)
    lawn1 = LawnProperties(1, "Vancouver", "canada", "1 Sennok Drive", 10, 10, 0.75, 1.25, 0)

    dataReq = LocationWeatherData()
    automateIrrigation  = AutoWatering(lawn1,locationWeatherData1)

    def testTimeMorningFalse(self):
        self.assertFalse(self.automateIrrigation.shouldWater())

    def testTimeMorningTrue(self):
        self.assertFalse(self.automateIrrigation.shouldWater())

    def testTimeEveningTrue(self):
        self.assertFalse(self.automateIrrigation.shouldWater())

    def testTimeEveningFalse(self):
        self.assertFalse(self.automateIrrigation.shouldWater())

