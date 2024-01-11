# str.format() -> optional method to users
#                 more control when displaying output

animal = "cow"
item = "moon"

# # print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("cow","moon"))
print("The {} jumped over the {}".format(animal,item))
print()

print("The {1} jumped over the {0}".format(animal,item)) #positional arguement of 1 and 0
print()

#keyword arguement
print("The {mammal} jumped over the {object}".format(mammal="bull",object="moon"))
print()

text = "The {} jumped over {}"
print(text.format(animal,item))
print()

####################################
name = "spade"
print("Hello , My name is {}".format(name))
#applying padding of 10 you can see by dragging cursor over both outputs
#include keyword and positional arguements as below "name:10"
# print("Hello , My name is {name:10}.Nice to meet yaa!".format(name))
print("Hello , My name is {:10}.Nice to meet yaa!".format(name))
print("Hello , My name is {:>10}.Nice to meet yaa!".format(name)) #right align
print("Hello , My name is {:<10}.Nice to meet yaa!".format(name)) #left align
print("Hello , My name is {:^10}.Nice to meet yaa!".format(name)) #center align


#######################################
num = 3.14159
num1 = 1000
print()
print("The number pi is {:.2f}".format(num))
print("The number pi is {:.3f}".format(num))
print("The number pi is {:.3f}".format(num1))
print("The number pi is {:,}".format(num1))
print("The number pi is {:b}".format(num1)) #binary
print("The number pi is {:o}".format(num1)) #octal

print("The number pi is {:x}".format(num1)) #hexadecimal lowercase
print("The number pi is {:X}".format(num1)) #hexadecimal uppercase  

print("The number pi is {:e}".format(num1)) #scientific lowercase    
print("The number pi is {:E}".format(num1)) #scientific uppercase   