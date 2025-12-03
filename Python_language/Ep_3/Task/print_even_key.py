# Task 12: Print keys whose values are even numbers
even_dict = {
    'a': 2,
    'b': 3,
    'c': 4,
    'd': 6,
    'f': 15
}

print("Using for loop :")
for k , v in even_dict.items():
    if v % 2 == 0:
        print(k)
        
print("************")
for k , v in even_dict.items():
    if v % 2 == 1:
        print(k)


