# Task 5: Remove items (pop, remove, del)
lists = [1, 4, "hello World", "Hello",  True, 2.3, 4.5]

# display the llist item
for a in lists:
    print(a, end = " ")
print()

print("Pop Operation :::>")
# pop Operation 
lists.pop(2)
for a in lists:
    print(a, end = " ")
print()
print("*****************")


print("Remove  Operation :::>")
# Remove Operation
lists.remove(2.3)
for a in lists:
    print(a, end = " ")
print()
print("*****************")


print("Delete  Operation :::>")
# del Operation
del lists[3]
for a in lists:
    print(a, end = " ")
print()
print("*****************")



