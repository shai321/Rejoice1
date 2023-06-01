class Vehicle:
    color="white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Bus1=Bus("School bus",200,50)
Car1=Car("Audi",300,5)
print(f"color: {Bus1.color}, name: {Bus1.name}, Max_speed: {Bus1.max_speed}, mileage: {Bus1.mileage}")
print(f"color: {Car1.color}, name: {Car1.name}, Max_speed: {Car1.max_speed}, mileage: {Car1.mileage}")