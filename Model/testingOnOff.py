from Model.autoWatering import AutoWatering
from Model.lawn import LawnProperties
import pymysql.cursors

class test():

    def mysqlConnection(self):
        connection = pymysql.connect(host="",
                                         user="turfswach",
                                         password="",
                                         db="",
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        if connection:
            return connection
        else:
            print("Connection expection error")

    def turnWater(self, status, lawn):
        connection = self.mysqlConnection()
        try:
            with connection.cursor() as cursor:
                sql = "Insert into logStatus (status, lawnID, city, country) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (status, lawn.lawnID, lawn.city, lawn.country))
                connection.commit()
        finally:
            connection.close()

def main():
    testWater = test()
    lawn1 = LawnProperties(1, "vancouver", "canada", "1 Sennok Drive", 10, 10, 0.75, 1.25,0)
    checkToIrrigate = AutoWatering(lawn1)

    if (checkToIrrigate.shouldWater):
        testWater.turnWater("1", lawn1)
    else:
        testWater.turnWater("0", lawn1)

main()
