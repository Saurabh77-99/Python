# args -> parameter that will pack all arguements into a tuple
#         useful so that function can accept a varying amount of arguement

def add(num1,num2):
    sum = num1 + num2
    return sum

print(add(1,2))

# asterisk *args
def addarg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(addarg(1,2,3))
print(addarg(1,2,3,4,5,6))

# tuple object doesn't support item assignment
def addstuff(*stuff):
    sum = 0
    # stuff[0] = 0 
    stuff = list(stuff)
    stuff[0]=0
    for i in stuff:
        sum += i
    return sum

print(addstuff(1,2,3,4,5,6))
