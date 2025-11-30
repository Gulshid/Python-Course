# Task 10: Remove duplicates from list
my_list = []
n = int(input("Enter the number that you want :"))

for a in range(n):
    number = int(input(f"Enter the value for {a + 1} :"))
    my_list.append(number)
    
    
print(" full list :")
for x in my_list:
    print(x, end= " ")
print()


unique_list = []

for val in my_list:
    if val not in unique_list:
        unique_list.append(val)

print("Without duplicate value list :")
print(unique_list)