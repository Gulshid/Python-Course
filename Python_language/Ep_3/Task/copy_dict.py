# Task 8: Copy a dictionary
dict_values = {
    'name': "Muhammad",
    'roll': 45,
    'marks': 450,
    'Semester' : '6th'
}

print('dict values using loop :')
print("Dict 1 :")
for a , b in dict_values.items():
    print(a + ":", b)
print()


print("****************")
print("Dict 2 :")
dict_2 = dict_values.copy()
for a , b in dict_values.items():
    print(a + ":", b)
print()