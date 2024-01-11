# function = a block of code , it is executed only when it is called
# invoking a function

def hello(name):
    print("hello "+name)
    print("have a nice day")

def hi(name,last,age):
    print("hello "+name+" "+ last)
    print("You are"+" "+str(age)+" years little" )
    print("have a nice day")

name = "bhai"
hello(name)

hello("bhaiya")
hello("Dude")

hi("Pub","Sub",21)