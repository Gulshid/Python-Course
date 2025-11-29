# Task 1: Create a list and display it
my_list = [1,2,3,"Hello", True, 3.4,6.7]

print("List Element :")
print(my_list)

# Task 2: Access list elements using index and loop
# Method 1 ===> index method
print("Indexing Method :")
print(my_list[0], my_list[1],  my_list[2],  my_list[3], my_list[4], my_list[5], my_list[6])

# Method 2 =====> loop method
print("Loop Method :")
for var in range(len(my_list)):
    print(my_list[var], end= " ")
print()

# Method 3 =====> Loop Method
print("Loop Method :")
for value in my_list:
    print(value, end= " ")
print()
