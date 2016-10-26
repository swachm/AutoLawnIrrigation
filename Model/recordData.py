import pymysql.cursors
import time
from Model.httpRequest import httpRequest
from Model.lawn import LawnProperties


class RecordData:
    def mysqlConnection(self):
        connection = ""
        try:
            connection = pymysql.connect(host="turf.cg0fwnlqgdqk.us-west-2.rds.amazonaws.com",
                                                   user="",
                                                   password="",
                                                   db="turf",
                                                   charset='utf8mb4',
                                                   cursorclass=pymysql.cursors.DictCursor)
        except pymysql.connections.err as error:
            print("MySQL Connection Error: {}".format(error))

        if connection:
            return connection
        else:
            print("Connection expection error")

    def logWeatherDataforLawn(self, data):
        connection = self.mysqlConnection()
        timeStamp = int(time.time())
        try:
            with connection.cursor() as cursor:
                sql = "Insert INTO weatherData" \
                      "(city, country, currentTemp, currentMaxTemp, currentMinTemp, " \
                      "currentHumidity, currentCloudiness, hoursRain, rainInLastXHour," \
                      "hoursSnow, snowInLastXHour, totalRainInNext24Hour, soilMoisture, " \
                      "soilTemp, sunrise, sunset, timeStamp)" \
                      "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (data.city, data.country, data.currentTemp, data.currentMaxTemp, data.currentMinTemp,
                             data.currentHumidity, data.currentCloudiness, data.rainHour, data.rainInLastXHour,
                             data.snowHour, data.snowInLastXHour, data.totalRainInNext24Hour, data.soilMoisture,
                             data.soilTemp, data.sunrise, data.sunset, timeStamp))
                connection.commit()
        finally:
            connection.close()

    def createLawn(self, lawn):
        timeStamp = int(time.time())
        connection = self.mysqlConnection()
        try:
            with connection.cursor() as cursor:
                sql = "Insert INTO lawnData" \
                      "(lawnID, area, waterQuantity, waterVolume, pipeCircumfrence, systemStatus, lawnName,timeStamp)" \
                      "values (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (lawn.lawnID, lawn.getArea(), lawn.waterQuantity, lawn.waterVolume(),
                                     lawn.pipeCircumfrence(), lawn.systemStatus, lawn.name,timeStamp))
                connection.commit()
        finally:
            connection.close()

    def updateLawnStatus(self, lawn):
        connection = self.mysqlConnection()
        try:
            with connection.cursor() as cursor:
                sql = "Update lawnData " \
                      "Set systemStatus = %s WHERE 'lawnID' = %s"
                cursor.execute(sql, (lawn.systemStatus, lawn.lawnID))
                connection.commit()
        finally:
            connection.close()

    def didItRainInLast24Hours(self, data):
        connection = self.mysqlConnection()
        timeStamp = int(time.time()) - 86400
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = "Select hoursRain, rainInLastXHour, hoursSnow, snowInLastXHour FROM weatherData " \
                      "WHERE 'city' = %s and 'country' = %s and 'timeStamp' >= %s"
                cursor.execute(sql, (data.city, data.country, timeStamp,))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

    def lastTimeLawnsWatered(self, lawn):
        connection = self.mysqlConnection()
        try:
            with connection.cursor() as cursor:
                sql = "Select timeStamp, systemStatus from lawnData where lawnID = %d"
                cursor.execute(sql, (int(lawn.lawnID),))
                result = cursor.fetchone()
        finally:
            connection.close()
        return result

'''
++++++++++++++++++++
+ LOGGING THE DATA +
++++++++++++++++++++

Data to Log into the server 19 variables for the weather provider

- city
- country
- currentTemp
- currentMaxTemp
- currentMinTemp
- currentHumidity
- currentCloudiness
- hoursRain
- rainInLastXHour
- hoursSnow
- snowInLastXHour
- rainInNext24Hour
- totalRainInNext24Hour
- systemStatus
- soilMoisture
- soilTemp
- sunrise
- sunset
- currentUnixTime

Data to Log into the server 19 variables for the each lawn in the system

- frontyardArea
- backyardArea
- waterThickness
- waterVolumeFront
- waterVolumeBack
- pipeCircumfrence
- systemStatusFrontyard
- systemStatusBackyard
'''
