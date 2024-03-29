# Exception -> events detected during execution that interrupts the flow of a program

try:
    numerator = int(input("Enter a number to divide:"))
    denominator  = int(input("Enter a number to divide by:"))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero !! Idiot !!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This finally block will always execute at the end !! ")