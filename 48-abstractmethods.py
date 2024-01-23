# abstract class -> prevent user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class -> a class which contains one or more abstract methods
# abstract methods -> a method that has declaration but doesn't have implementation

from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This car is stopped")

# vehicle=Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

