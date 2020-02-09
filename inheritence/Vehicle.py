class Vehicle:
    """Vehicle Class.
    """
    def __init__(self, driverName, numOfSeats, numOfWheels):
        """Constructor.
        
        Arguments:
            driverName {String} -- Driver's name.
            numOfSeats {Integer} -- Number of seats.
            numOfWheels {Integer} -- Number of wheels.
        """
        self.driverName = driverName
        self.numOfSeats = numOfSeats
        self.numOfWheels = numOfWheels

# firstVehicle = Vehicle("Amit", 2, 4)

# print(firstVehicle.driverName)
# print(firstVehicle.numOfSeats)
# print(firstVehicle.numOfWheels)