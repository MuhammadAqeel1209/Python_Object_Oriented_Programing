class Vehicle:
    def Into(self):
        print("There are different Vehicles")
    def Speed(self):
        print("Different cars has different speed")  

class Truck(Vehicle):
    def Speed(self):
        print("This is Slow Speed")

class Car(Vehicle):
    def Speed(self):
        print("This is Faster")

def CheckSpeed(Vehicles):
    return Vehicles.Speed()

Vec = Vehicle()
Car = Car()
Tru = Truck()

# Vec.Into()
# Vec.Speed()
CheckSpeed(Vec)
print("-----------------")

# Car.Into()
# Car.Speed()
CheckSpeed(Car)
print("-----------------")

CheckSpeed(Tru)
# Tru.Into()
# Tru.Speed()
print("-----------------")