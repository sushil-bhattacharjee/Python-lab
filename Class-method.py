class Car:
    number_of_wheels = 4

    def __init__(self, color, sunroof="up"):
        self.color = color
        self.sunroof = sunroof

    def drive(self):
        print("It's BOND Car")

    def topdown(self):
        self.sunroof = "down"

    def turn(self, direction):
        print(f"Turning{direction}")


my_new_car = Car("blue")

print(f"This car has {my_new_car.number_of_wheels} wheels")
print(f"Currently the sunroof is {my_new_car.sunroof}")
my_new_car.topdown()
print(f"Currently the sunroof is {my_new_car.sunroof}")

#my_new_car.drive("RIGHT")