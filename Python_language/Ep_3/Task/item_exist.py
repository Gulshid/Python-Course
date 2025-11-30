# Task 12: Check if an item exists in list

num = []
x = int(input("Enter the Number :"))

for i in range(x):
    user_input = int(input(f"Enter the value for {i + 1} :"))
    num.append(user_input)
    
    
print("List is : ", num)
value = int(input("Enter the value for check:"))

if value in num:
    print(f"The Item {value} is Exist in List :>")
else:
    print(f"The Item {value} is Not Exist in List :>")