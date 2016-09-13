import RPi.GPIO as GPIO                              #sudo apt-get install python-rpi.gpio


from Model.autoWatering import AutoWatering

class RasberyConnections:

    def __init__(self):
        GPIO.setup(17, GPIO.OUT)  # set up pin 17     #frontyard
        GPIO.setup(18, GPIO.OUT)  # set up pin 17     #frontyard
        #Get total number of lawn objects and intitalize that many pins default set to two pins

    #Turn on at 6AM or 7PM depending on how much water is needed
    def turnWaterOn(pin):
        GPIO.output(int(pin), 1)
        return;

    def turnWaterOff(pin):
        GPIO.output(int(pin), 0)
        return;

def main():
    # berryConnection = rasberyConnections()
    #
    # #Do this all the lawn setups and check in the other files to see if the data allows for watering
    # if (AutoWatering.shouldWater):
    #     berryConnection.turnWaterOn(17)
    # else:
    #     berryConnection.turnWaterOff(17)

main()