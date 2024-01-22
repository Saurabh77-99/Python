from cars import Car

car_1 = Car("Chevy","corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

# Class variable wheels = 4 its default , it can be changed by given below of car_1
Car.wheels = 2 #this will affect whole class and applied to all instances 
car_1.wheels = 2 # this will affect only car_1 object of instance

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels) #without creating an object