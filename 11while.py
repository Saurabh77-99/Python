# while - a statement that will execute its block of code as long as its condition remains true

# while 1==1:
#     print("Help !! I am stuck in loop!")

name = ""
while len(name) == 0:
    name = input("enter your name:")

print("Hello "+name)

# other way 
name = None
while not name:
    name = input("Enter your name:")

print("Hello "+name)