import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def VehicleDEcoder(obj):
    return Vehicle(obj['name'],obj['engine'],obj['price'])

vehicle = json.loads('{"name": "Toyota Rav4","engine":  "2.5L","price": 32000}', object_hook=VehicleDEcoder)
print(vehicle.name,vehicle.engine,vehicle.price)
print(type(vehicle))
