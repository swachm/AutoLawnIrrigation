import math

class LawnProperties():

    def __init__(self, lawnID, city="", country = "", name="lawn", length=0, width=0, pipeDiameter=0, waterQuantity=1.25, systemStatus=0):
        self.lawnID = lawnID
        self.city = city
        self.country = country
        self.name = name
        self.length = length
        self.width = width
        self.pipeDiameter = pipeDiameter
        self.waterQuantity = waterQuantity
        self.systemStatus = systemStatus

    @property
    def lawnID(self):
        return self._lawnID

    @lawnID.setter
    def lawnID(self, value):
        self._lawnID = str(value)

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

    @lawnID.setter
    def lawnID(self, value):
        self._lawnID = int(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = float(value)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = float(value)

    @property
    def pipeDiameter(self):
        return self._pipeDiameter

    @pipeDiameter.setter
    def pipeDiameter(self, value):
        self._pipeDiameter = float(value)

    @property
    def systemStatus(self):
        return self._systemStatus

    @systemStatus.setter
    def systemStatus(self, value):
        self._systemStatus= int(value)

    @property
    def lawnID(self):
        return self._lawnID

    @lawnID.setter
    def lawnID(self, value):
        self._lawnID = int(value)

    @property
    def waterQuantity(self):
        return float(self._waterQuantity)

    @waterQuantity.setter
    def waterQuantity(self, value):
        self._waterQuantity = float(value)

    def getArea(self):
        return float(self._width * self._length)

    def pipeCircumfrence(self):
        return float(math.pi * self._pipeDiameter)

    def waterVolume(self):
        return float(self.getArea() * self._waterQuantity)