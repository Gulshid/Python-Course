# Task 4: Modify list items
fruits = ["Apple", "Banana", "Orange", "Mango"]
print("Before modify :")
for val in fruits:
    print(val, end = " ")
print()

print("After modify :")
fruits[3] = "Apple"
fruits[1] = "Mango"
fruits[2] = 250
for val in fruits:
    print(val, end = " ")
print()

