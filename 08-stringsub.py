#slicing - create a substring by extracting from another string
# indexing[] or slice()
# [start:stop:step]

name = "Iron-Man"

first_name = name[0:4]
ofirst_name = name[:4]

last_name = name[4:]
olast_name = name[4:7]

stepsub = name [0:8:2]
ostepsub = name [0:8:3]
mstepsub = name [::3]

reversed = name[::-1]

website = "http://google.com"
web = "http://wikepedia.com"
slice = slice(7,-4)

print(website[slice])
print(web[slice])

print(first_name)
print(ofirst_name)

print(last_name)
print(olast_name)

print(stepsub)
print(ostepsub)
print(mstepsub)

print(reversed)