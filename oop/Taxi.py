class Taxi:
    """Numer of taxis.
    
    Returns:
        Integer -- Number of taxis.
    """
    numOfTaxis = 0

    
    def __init__(self, driverName, onDuty, cities, color):
        """Constructor
        
        Arguments:
            driverName {String} -- Driver's name.
            onDuty {Boolean} -- Duty status.
            cities {List} -- List of cities, the taxi can operate.
            color {String} -- Color of the taxi.
        """
        self.driverName = driverName
        self.onDuty = onDuty
        self.cities = cities
        self.__color = color
        self.numOfPassengers = 0
        Taxi.numOfTaxis += 1
    
    def __addText(self, text):
        """Add medical text at the end of the give string.
        
        Arguments:
            text {String} -- Text to be appended to.
        
        Returns:
            String -- Return the modified text.
        """
        return text + ' Medical'

    def getColor(self):
        """Get the color of the taxi.
        
        Returns:
            String -- Color of the taxi.
        """
        modifiedColor = self.__addText(self.__color)
        return modifiedColor

    def setColor(self, newColor):
        """Set the color of the taxi.
        
        Arguments:
            newColor {String} -- New color of the taxi.
        """
        self.__color = newColor

    def getDriverName(self):
        """Get the driver's name.
        
        Returns:
            String -- Driver's name.
        """
        return self.driverName

    def setDriverName(self, newDriverName):
        """Set the driver's name.
        
        Arguments:
            newDriverName {String} -- New driver's name.
        """
        self.driverName = newDriverName

    def setOnDuty(self, newOnDuty):
        """Set on duty status.
        
        Arguments:
            newOnDuty {Boolean} -- New duty status.
        """
        self.onDuty = newOnDuty

    def setCities(self, newCities):
        """Set the list of cities.
        
        Arguments:
            newCities {List} -- New cities list.
        """
        self.cities = newCities

    def pickUpPassengers(self, numOfPassengers):
        """Pickup the passengers.
        
        Arguments:
            numOfPassengers {Integer} -- Number of passengers picked up.
        """
        self.numOfPassengers += numOfPassengers

    @classmethod
    def getNumberOfTaxis(cls):
        """Get the number of taxis created.
        
        Returns:
            Integer -- Return the number of taxis.
        """
        return cls.numOfTaxis
    


firstTaxi = Taxi("Suman", True, ['Kathmandu', 'Bhaktapur'], 'Yellow')
print("Driver's name : " + firstTaxi.driverName)
print("On duty : " + str(firstTaxi.onDuty))
print("Color: " + str(firstTaxi.getColor()))
print("Number of Taxis : " + str(Taxi.numOfTaxis))

secondTaxi = Taxi("Suman", True, ['Kathmandu', 'Bhaktapur'], 'Yellow')
print("Number of Taxis : " + str(Taxi.numOfTaxis))
thirdTaxi = Taxi("Suman", True, ['Kathmandu', 'Bhaktapur'], 'Yellow')
print("Number of Taxis : " + str(Taxi.numOfTaxis))