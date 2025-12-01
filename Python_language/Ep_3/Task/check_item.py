# Task 7: Check if value exists in tuple
tuple_num = (2,3,4,5,6)

print("Tuple values :")
print(tuple_num)

num = int(input("Enter the value :"))

if num in tuple_num:
    print(f"The num {num} is exist in tuple")
else:
    print(f"The num {num} is not exist in tuple ")