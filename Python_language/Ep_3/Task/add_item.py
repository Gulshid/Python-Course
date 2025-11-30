# Task 3: Add items using append, insert, extend
list_py = [1, 4, 7, "Hi", True, 2.3,  6.7]

# display using loop method
for item in list_py:
    print(item, end = " ")
print()

print("Append Operation :")
# Apppend Operation
list_py.append(23)
for i in list_py:
    print(i, end= " ")
print()


print("Insert Operation :")
# Insert Operation
list_py.insert(2, 5)
for i in list_py:
    print(i, end= " ")
print()

print("Extend Operation :")
# Extend Operation
list_py.extend(["Hello", "World", 2, 4.5, False, True])
for i in list_py:
    print(i, end= " ")
print()

