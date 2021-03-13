class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass


schoolBus = Bus("School Bus", 100, 50000)
print("Vehicle name:", schoolBus.name,", max speed -", schoolBus.max_speed, ", mileage -", schoolBus.mileage)
