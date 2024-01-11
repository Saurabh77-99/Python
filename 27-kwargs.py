# **kwargs -> parameter that will pack all arguements into dictionaries
#             useful so that a function can accept a varying amount of keyword arguement

# def hello(first,last):
#     print("Hello "+first+" "+last)

# hello(first="Abc",last="Pun",middle="ob")

def hkwargs(**kwargs):
    # print("hello "+ kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hkwargs(first='bun',middle='dude',last="cup")
print()
hkwargs(title="Mr.",first='bun',middle='dude',last="cup")