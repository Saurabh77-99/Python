# set - a collection which is unordered , unindexed and no duplicate values
# the ouput must not be in the same order
# set is faster than list and doesnt allows duplicate values
utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

# utensils.add("hanky")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)


for x in utensils:
    print(x)

# union of two sets
dinner_table = utensils.union(dishes)
print(dinner_table)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))