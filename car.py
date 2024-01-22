class Car:
    #constructor
    def __init__(self,make,model,year,color):
        #attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    #methods
    def drive(self):
        print("This "+ self.model + " is driving")

    def stop(self):
        print("This "+ self.model + " is stopped")