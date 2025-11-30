# Task 9: Find largest and smallest number in list
num = []
a = int(input("Enter the Number that you want :"))

for i in range(a):
    x = int(input(f"Enter the value for {i + 1} :"))
    num.append(x)
    
    
print("Display the full list :")
for z in num:
    print(z, end = " ")
print()

# largest and smallest value 
largest = num[0]
smallest = num[0]

for val in num:
    if val > largest:
        largest = val
    
    if val < smallest:
        smallest = val


print("The Largest value in List :", largest)
print("The Smallest value in List :", smallest)