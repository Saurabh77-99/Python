# list - to store a multiple item in single variable

food = ["pizza","hamburger","hotdog","sphagetti","pudding"]

food[0] ="sushi"

print(food[0])
print()

food.append("ice-cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:
    print(x)
