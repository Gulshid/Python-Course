# 23.Write a function that removes duplicates from a list.
def unique_list(num):
    unique = []
    for value in num:
        if value not in unique:
            unique.append(value)
            
    return unique


# function call
my_list = [1,2,2,4,5,6,6,7,8,7]
print("The final list :", unique_list(my_list))