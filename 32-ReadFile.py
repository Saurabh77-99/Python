try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That File was not found :!")
    
# print(file.closed)