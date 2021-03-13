class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehicleObj = Vehicle(123, 456)
print("Vehicle max speed - ", vehicleObj.max_speed, ", mileage - ", vehicleObj.mileage)