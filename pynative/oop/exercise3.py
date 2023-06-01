class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Car(Vehicle):
    pass

a=Car("shai",200,50)
print(a.name)
print(a.max_speed)
print(a.mileage)