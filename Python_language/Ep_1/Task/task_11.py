#11. Swap Two Number With and Without third Variable
num_1 = 5
num_2 = 10
# 1. With Third variable Method 
print("Before Swapping :")

print(f"The value of Num_1 : {num_1}. and num_2 : {num_2}")

print("After Swapping :")

#  logic for Swapping using Third variable
num_3 = num_1 # num_3 = 5
num_1 = num_2 # num_1 = 10
num_2 = num_3 # num_2 = 5

print(f"The value of Num_1 : {num_1}. and num_2 : {num_2}")

print("******************")

# 2. Without Third Variable Method 

value_1 = 2
value_2 = 4

print("Before Swapping :")
print(f"The value_1 : {value_1} and value_2 : {value_2}")
#  logic for swapping using Without Third Variable Method 

print("After Swapging :")

value_1 = value_1 + value_2 # 2 + 4 = value_1 ===> 6
value_2 = value_1 - value_2 # 6 - 4 = value_2 ===> 2
value_1 = value_1 - value_2 # 6 - 2 = value_1 ==>  4
print(f"The value_1 : {value_1}. and value_2 : {value_2}")