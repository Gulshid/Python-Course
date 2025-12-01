# Task 5: Find max and min in numeric tuple
tuple_value = (2,4,6,12,15)

# display tuple element 
print("Tuple element :")
print(tuple_value)

print("*************")
# max and min find inside the tuple
Max = tuple_value[0]
Min = tuple_value[0]


for x in tuple_value:
    if x > Max:
        Max = x
        
    if x < Min:
        Min = x

print("*************")
print(f"Max value in Tuple : {Max}")
print(f"Min value in Tuple : {Min}")