from Vehicle import Vehicle

class Bus(Vehicle):
    """Vehicle class
    
    Arguments:
        Vehicle {Vehicle} -- Vehicle class.
    """
    def __init__(self, driverName, numOfSeats, numOfWheels, color):
        """Constructor
        
        Arguments:
            driverName {String} -- Driver's name.
            numOfSeats {Integer} -- Number of seats.
            numOfWheels {Integer} -- Number of wheels.
            color {[type]} -- Color of the vehicle.
        """

        # Initializa the parent class.
        super().__init__(driverName, numOfSeats, numOfWheels)
        self.color = color


firstBus = Bus("Amit", 3, 4, True);

print(firstBus.driverName)
print(firstBus.numOfSeats)
print(firstBus.numOfWheels)
print(firstBus.color)