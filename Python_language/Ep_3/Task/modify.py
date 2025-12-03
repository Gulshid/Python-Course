# Task 4: Modify existing values
student = {
    'name': "Muhammad",
    'roll no':391,
    'marks':450,
    'age': 21,
    'city':'peshawar',
    'Grade':'B'
}

print("Dict values using loop :")
for k, v in  student.items():
    print(k + ":", v)
print()

print("*************")
print("Single value modify :")
student['name'] = "Gulshid Zada"
student['age'] = 23
for k, v in  student.items():
    print(k + ":", v)
print()


print("*************")
print("Multiple value modify :")
student.update({
    'name':"ALi",
    'age': 22,
    'marks': 400,
    'city':"islamabad",
    'Grade':'A'
})
for k, v in  student.items():
    print(k + ":", v)
print()
