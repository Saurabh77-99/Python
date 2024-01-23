#concept where the class of object is less important than the methods/attributes that
# class type is not checked if min methods/attributes are present
# "if it walks like a duck,and it quacks like a duck then it must be duck"

class Duck:

    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("The duck is talking")

class Chicken:

    def walk(self):
        print("The chicken is walking")

    def talk(self):
        print("The chicken is talking")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)