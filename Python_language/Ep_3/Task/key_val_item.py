# Task 2: Access keys, values, items
Student_Dict = {
    'name': "Muhammad",
    'roll no ': 391,
    'Semester': '5th',
    'Marks': 460,
    'Persentage':'86%',
    'Department': "BS CS"
}
# display the dict value 
print("dict values :")
print(Student_Dict)

print("****************")
print("Only keys of dict :")
print(Student_Dict.keys())

print("****************")
print("Only values :")
print(Student_Dict.values())

print("****************")
print("Key value pairs (item) :")
print(Student_Dict.items())

print("****************")
print("Using loop (key):")
for k in Student_Dict.keys():
    print(k, end = " ")
print()

print("****************")
print("Using loop (values):")
for d in Student_Dict.values():
    print(d, end = " ")
print()

print("****************")
print("Using loop (key - value paris (item)):")
for key, value in Student_Dict.items():
    print(key+":", value)



