class Bus:
    """Bus Class
    
    Returns:
        Bus -- Buc class.
    """
    numOfBuses = 0
    
    def __init__(self, driverName, color, numOfSeats):
        """Constructor
        
        Arguments:
            driverName {String} -- Driver's name.
            color {String} -- Color of the bus.
            numOfSeats {Integer} -- Number of seats.
        """
        self.driverName = driverName
        self.color = color
        # Private varible.
        self.__numOfSeats = numOfSeats
        Bus.numOfBuses += 1

    def getNumOfSeats(self):
        """Get the number of seats.
        
        Returns:
            Integer -- Number of seats.
        """
        return self.__numOfSeats

    def setNumOfSeats(self, numOfSeats):
        """Set the number of seats.
        
        Arguments:
            numOfSeats {Integer} -- Number of seats.
        """
        self.__numOfSeats = numOfSeats
    
firstBus = Bus("Amit", "Blue", 10)
print("Driver Name : "+ firstBus.driverName)
firstBus.driverName = "Ashish";
print("Driver Name : "+ firstBus.driverName)
print("Color : " + firstBus.color)
print("Num of seats: " + str(firstBus.getNumOfSeats()))
print("Number of buses: " + str(Bus.numOfBuses))
firstBus.setNumOfSeats(20)
print("Num of seats: " + str(firstBus.getNumOfSeats()))

print("\n#### Second Bus")

secondBus = Bus("Suman", "Red", 11)
print("Driver Name : "+ secondBus.driverName)
print("Color : " + secondBus.color)
print("Num of seats: " + str(secondBus.getNumOfSeats()))
secondBus.setNumOfSeats(111)
print("Num of seats: " + str(secondBus.getNumOfSeats()))
print("Number of buses: " + str(Bus.numOfBuses))

