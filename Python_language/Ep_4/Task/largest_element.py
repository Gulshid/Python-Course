# 22.Write a function that returns the largest element in a list.
def largest_Element(number):
    largest = number[0]
    
    for x in number:
        if x > largest:
            largest = x
    return largest


# function call
my_list = [1,3,6,20,23,9]
print("The largest element in list is :",largest_Element(my_list))
        