from Vehicle import Vehicle

class Taxi(Vehicle):
    """Taxi class
    
    Arguments:
        Vehicle {Vehicle} -- Vehicle parent class.
    
    Returns:
        Taxi -- Taxi class.
    """
    def __init__(self, driverName, numOfSeats, numOfWheels, onDuty):
        """Constructor
        
        Arguments:
            driverName {String} -- Driver's name.
            numOfSeats {Integer} -- Number of seats.
            numOfWheels {Integer} -- Number of wheels.
            onDuty {Boolean} -- Duty status.
        """
        super().__init__(driverName, numOfSeats, numOfWheels)
        self.onDuty = onDuty

    def __str__(self):
        """Override the built-in function
        
        Returns:
            String -- String format of the class.
        """
        return "Taxi driver is = " + self.driverName + ". The taxi has " + str(self.numOfSeats) + " number of seats."



firstTaxi = Taxi("Suman", 3, 4, True);

print(firstTaxi)

print(firstTaxi.driverName)
print(firstTaxi.numOfSeats)
print(firstTaxi.numOfWheels)
print(firstTaxi.onDuty)