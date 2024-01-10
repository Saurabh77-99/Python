# convert one data type to another

x = 1
y = 2.0
z = "3"

# int(y) converting float to int
x = float(x)
y = int(y)
y = str(y)
z = int(z)

print("X is :" + str(x))
print("Y is :" + str(y))
print("Z is :" + str(z*3))

print(type(x))
print(type(y))
print(type(z*3))
# print(int(y))