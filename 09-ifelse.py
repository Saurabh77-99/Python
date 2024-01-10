#if-else = is a block of code that will execute if its condition is true!
#nested 
age = int(input("How old are you?: "))

if age >= 18:
    print("you are an adult!")
if age == 100: #comparison operator
    print("You have lived 10 decades on earth")   
elif age < 0:
    print("you haven't been born yet!!")
elif age >=13 and age<=18:
    print("You are a teen!!")
else:
    print("You are a kid !!")
