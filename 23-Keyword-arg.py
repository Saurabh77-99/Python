# arguement preceded by identifier when we pass them to function
# the order of the arguements doesn't matter,unlike positional arguements
#  Pyhton knows the name of the arguements that our funtcion receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(first="Abc",middle="Bun",last="Pun")
hello(middle="Bun",first="Abc",last="Pun")