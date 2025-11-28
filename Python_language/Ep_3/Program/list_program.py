# List 
number = [1,2,3, 4.5, 6.7, 'Hello WOrld', True]

# Method 1 
print("Method No 1:")
print(number)

# Method 2
print("Method No 2:")
for w in range(len(number)):
    print(number[w], end = " ")

print()
# Method 3
print("Method No 3 :")
for item in number:
    print(item, end= " ")