# Dictionary is a changeable,unordered collection of unique key:value pairs
#            fast because they use hashing,allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
# capitals.clear()

print(capitals['Russia'])
# print(capitals['Germany']) ->error
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print()

for key,value in capitals.items():
    print(key,value)
