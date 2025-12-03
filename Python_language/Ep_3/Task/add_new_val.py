# Task 3: Add new key-value pairs
student = {
    'name':'Ali',
    'roll no':390,
    'marks':399
}

print("dict value :")
print(student)

print("***********")
print("SIngle key value pair :")
student['Semester'] = '5th'
print(student)

print("***********")
print("Multiple key value pairs :")
student.update({
    'Department':"BS CS",
    'Section':'B',
    'Grade':'A'
})
print(student)

print("***********")
# using loop
print("using loop :")
for key, value in student.items():
    print(key + ":",value)
print()
