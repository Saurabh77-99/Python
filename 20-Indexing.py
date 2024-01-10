# index operator [] = gives access to a sequences element (str,list,tuples)

name = "ben Code!"

if(name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[:4].upper()
last_name = name[4:].lower()
last_char = name[-1] 

print(first_name)
print(last_name)
print(last_char)