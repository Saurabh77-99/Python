# sort() method -> used with lists
# sort() function ->used with iterables

#list
students = ["Squid","Sandy","Patrick","Sponge","Mr.Kube"]
# twp optional keyword args
students.sort()
# students.sort(reverse=True)
# sort method is not going to work in tuples
for i in students:
    print(i)

print()
print()
# tuple
students = ("Squid","Sandy","Patrick","Sponge","Mr.Kube")

sorted_students = sorted(students)
# sorted_students = sorted(students,reverse=True)
for i in sorted_students:
    print(i)

print()
print()

# Level 2
#list of tuples
students = [("Squid","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Sponge","B",20),
            ("Mr.Kube","C",78)]

# 1 for column of grade i.e 0 1 2
grade = lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print(i)

print()
print()
age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)

print()
print()
#tuples of tuples
studentss = (("Squid","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Sponge","B",20),
            ("Mr.Kube","C",78))

ages = lambda agess:agess[2]
sorted_studentss = sorted(studentss,key=age,reverse=True)

for i in sorted_studentss:
    print(i)