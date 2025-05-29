class vehicle:
    def maxspeed(self):
        pass

class BMW(vehicle):
    def maxspeed(self):
        return "Audi maxspeed is 200 for MPH"
    def fueltype(self):
        return "Fuel Type-Petrol"

class Ferari(vehicle):
    def maxspeed(self):
        return "Benz maxspeed is 250 for MPH"
    def fueltype(self):
        return "Fuel Type-Diesel"

o=[BMW(), Ferari()]

for i in (o):
    print(i.maxspeed())
    print(i.fueltype())