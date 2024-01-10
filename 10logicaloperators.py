# and , or - used to check two or more conditional statements

temp = float(input("What is the temp outside? :"))

if not(temp >= 0 and temp <= 30):
    # print("The temperature is good today")
    # print("go outside!")
    print("The temperature is bad today")
    print("go inside!")
elif not(temp < 0 or temp >30):
    print("The temperature is good today")
    print("go outside!")
    # print("The temperature is bad today")
    # print("go inside!")