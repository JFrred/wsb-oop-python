class Vehicle:

    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("Volvo", 120, 1000)
car = Car("Jaguar", 200, 500)

print("Color:", bus.color)
print("Color:", car.color)