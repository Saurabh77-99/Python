#nested functions - function calls inside other function calls
# innermost function callss are resolved first
# returned value is used as arguement for the next outer function

# num = input("Enter a whole positive number:")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# another way of writing same code
print(round(abs(float(input("Enter a whole positive number:")))))