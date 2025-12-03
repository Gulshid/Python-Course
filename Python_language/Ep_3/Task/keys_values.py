# Task 6: Loop through keys and values
dict_val = {
    'name': "Muhammad",
    'roll': 12,
    'marks': 300,
    'grade': "B"
}

print("Only keys using loop :")

for key in dict_val.keys():
    print(key)
print()

print("Only values using loop :")

for val in dict_val.values():
    print(val)
print()



print("Key value pairs using loop :")
for key, val in dict_val.items():
    print(key + ":" , val)
print()
    
