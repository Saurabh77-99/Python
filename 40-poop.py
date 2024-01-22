#  object is an instance of class
from car import Car

car_1 = Car("Chevy","corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

#when we call we need parameters but we don't need here!
car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()