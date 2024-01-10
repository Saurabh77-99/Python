rows = int(input("How many Rows? :"))
columns = int(input("How many columns? :"))
symbol = input("How many symbol to use? :")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()    