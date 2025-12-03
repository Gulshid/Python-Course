# Task 5: Remove elements (pop, popitem, del)
student = {
    'name': "Ali",
    'roll': 200,
    'marks': 456,
    'grade':'A+',
    'city':"Lahore"
}

print("Using loop dict values :")
for key, val in student.items():
    print(key + " : ", val)
print()



# pop function
element_removed = student.pop('marks')
print("Removed Element :",element_removed )
for key, val in student.items():
    print(key + " : ", val)
print()


print("**************")
# popitem function
element_popitem = student.popitem()
print("popitem Element :", element_popitem)
for key, val in student.items():
    print(key + " : ", val)
print()

print("**************")

# del function
print("Delete function :")
del student['roll']
for key, val in student.items():
    print(key + " : ", val)
print()




