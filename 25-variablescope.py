# scope = The region that a variable is recognise
# a variable is only available from inside the region it is created
# a global and locally scoped versions of a variable can be created

# RULE -> LEGB = Local variables first , Enclosed variables, Global variables , Built-in

name = "Bun" #a global scope (variable inside and outside functions)

def display_name():
    name = "Code" #local scope(available only inside this function)
    print(name)

display_name()
print(name)