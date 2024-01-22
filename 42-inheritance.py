class Animal:

    alive = True

    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("The rabbit is running")

class Fish(Animal):
    
    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("The Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
