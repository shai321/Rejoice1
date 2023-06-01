import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self,a):
        return a.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
js=json.dumps(vehicle, indent=3, cls=VehicleEncoder)

print(js)