# Task 7: Check if key exists
dict_key = {
    'name': "Gulshid Zada",
    'roll': 391,
    'Marks': 450,
    'city': "Peshawar",
    'grade': 'A'
}

key = input("Enter any key :")

if key in dict_key:
    print("The Key is Exist in Dict ==>")
else:
    print("The Key is not Exist in Dict ==>")


