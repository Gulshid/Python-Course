# 7.Write a function that returns the square of a number.
def square(num):
    return num * num
    # return num * num * num ===> cube operation

# function call
print(f"The sqaure of num is :{square(4)}")
print("***********")
n = int(input("Enter the value for n :"))
print(f"The Square of {n} is {square(n)}")