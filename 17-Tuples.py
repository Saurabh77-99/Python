# tuple - collection which is ordered and unchangeable
#         used to group together related data

# paranthesis (0 1 2)
student = ("Stark",18,"male")

print(student.count("Stark"))
print(student.index("male"))

for x in student:
    print(x)

if "Stark" in student:
    print("Stark is here bro!")